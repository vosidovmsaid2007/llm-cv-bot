import io
import asyncio
import json
from datetime import datetime
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from docx import Document
from PyPDF2 import PdfReader
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()

def load_vacancies_from_json(filename=config.FILES["vacancies_json"]):
    """Загружает данные вакансий из json файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке JSON: {e}")
        return []

# /start command
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = f"{config.MESSAGES['start_welcome']}\n\n{config.MESSAGES['start_commands']}\n\n{config.MESSAGES['start_resume_desc']}\n{config.MESSAGES['start_search_desc']}"
    await message.answer(welcome_text)

# /resume command
@dp.message(Command("resume"))
async def cmd_resume(message: types.Message):
    await message.answer(config.MESSAGES["resume_request"])

@dp.message(F.text & ~F.text.startswith("/"))
async def handle_text_message(message: types.Message):
    await message.answer(config.MESSAGES["resume_request"])

@dp.message(F.photo | F.video | F.audio | F.voice | F.video_note | F.sticker | F.animation)
async def handle_other_media(message: types.Message):
    await message.answer(config.MESSAGES["resume_request"])

@dp.message(F.document)
async def handle_resume_file(message: types.Message):
    if not message.document.file_name.lower().endswith(tuple(config.TEXT_EXTRACTION["supported_formats"])):
        await message.answer(config.MESSAGES["wrong_file_type"])
        return
    
    if message.document.file_size > config.FILES["max_size_bytes"]:
        await message.answer(config.MESSAGES["file_too_large"])
        return
    
    loading_message = await message.answer(config.MESSAGES["file_reading"])
    
    try:
        file = await bot.get_file(message.document.file_id)
        file_data = await bot.download_file(file.file_path)
        text = extract_text_from_resume(file_data, message.document.file_name)
        
        await loading_message.delete()
        
        await message.answer(f"{config.MESSAGES['resume_text_prefix']}{text}")
        
    except Exception as e:
        await loading_message.delete()
        await message.answer(f"❌ Ошибка при обработке файла: {str(e)}")

def extract_text_from_resume(file_data: io.BytesIO, filename: str) -> str:
    ext = filename.lower().split(".")[-1]
    text = ""
    if ext == "pdf":
        reader = PdfReader(file_data)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
    elif ext == "docx":
        doc = Document(file_data)
        text = "\n".join(p.text for p in doc.paragraphs)
    return text.strip()

# /search command
@dp.message(Command("search"))
async def cmd_search(message: types.Message):
    vacancies_data = load_vacancies_from_json()
    
    if not vacancies_data:
        await message.answer(config.MESSAGES["vacancies_not_found"])
        return
    
    keyboard_buttons = []
    for vacancy in vacancies_data:
        keyboard_buttons.append([types.InlineKeyboardButton(
            text=f"{vacancy['title']} - {vacancy['company']}", 
            url=vacancy['url']
        )])
    
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=keyboard_buttons)
    await message.answer(config.MESSAGES["vacancies_found"].format(count=len(vacancies_data)), reply_markup=keyboard)

async def main():
    print(config.MESSAGES["bot_started"])
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
