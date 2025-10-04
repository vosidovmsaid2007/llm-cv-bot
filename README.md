# LLM CV Bot

Простой тг-бот для анализа резюме и поиска вакансий с API для извлечения навыков.

## Команды:

- `/start` - Приветствие
- `/resume` - Загрузка и анализ резюме (PDF/DOCX)
- `/search` - Поиск подходящих вакансий

## Технологии

### Backend
- **Python 3.8+**
- **aiogram** - Telegram Bot API
- **FastAPI** - REST API
- **PyPDF2** - Обработка PDF файлов
- **python-docx** - Обработка DOCX файлов


## Запуск проекта

### 1. Клонирование репозитория
```bash
git clone <repository-url>
cd llm-cv
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка конфигурации
Отредактируйте `config.py`:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
```

### 4. Запуск бота
```bash
python bot.py
```

### 5. Запуск API (опционально)
```bash
cd api
uvicorn api:app --reload
```


## Логирование

Бот выводит информацию о:
- Запуске и остановке
- Ошибках загрузки файлов
- Ошибках обработки JSON
- Ошибках извлечения текста
