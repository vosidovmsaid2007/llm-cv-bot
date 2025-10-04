BOT_TOKEN = ""

MESSAGES = {
    "start_welcome": "Добро пожаловать в бот поиска работы!",
    "start_commands": "Доступные команды:",
    "start_resume_desc": "/resume - отправить резюме для анализа",
    "start_search_desc": "/search - найти подходящие вакансии",
    "resume_request": "Пожалуйста, отправьте PDF или DOCX файл резюме.",
    "wrong_file_type": "Пожалуйста, отправьте PDF или DOCX файл резюме.",
    "file_too_large": "Файл слишком большой! Максимальный размер: 5MB",
    "file_reading": "Читаю файл, пожалуйста подождите...",
    "resume_text_prefix": "Текст из вашего резюме:\n\n",
    "vacancies_not_found": "Не удалось загрузить данные вакансий",
    "vacancies_found": "Найдено {count} вакансий:",
    "bot_started": "Бот запущен"
}

FILES = {
    "vacancies_json": "vacancies.json",
    "max_size_mb": 5,
    "max_size_bytes": 5 * 1024 * 1024
}

TEXT_EXTRACTION = {
    "supported_formats": [".pdf", ".docx"]
}

SKILLS = [
    # Programming Languages
    "Python", "JavaScript", "TypeScript", "Java", "C#", "C++", "C", "Go", "Rust", "PHP",
    "Ruby", "Swift", "Kotlin", "Scala", "R", "MATLAB", "Perl", "Haskell", "Clojure", "Erlang",
    
    # Web Development
    "HTML", "CSS", "React", "Vue.js", "Angular", "Node.js", "Express.js", "Django", "Flask",
    "FastAPI", "Spring Boot", "Laravel", "Symfony", "ASP.NET", "jQuery", "Bootstrap", "SASS", "LESS",
    "Webpack", "Vite", "Next.js", "Nuxt.js", "Gatsby", "Svelte", "Ember.js", "Backbone.js",
    
    # Databases
    "SQL", "MySQL", "PostgreSQL", "MongoDB", "Redis", "Elasticsearch", "Cassandra", "DynamoDB",
    "SQLite", "Oracle", "SQL Server", "MariaDB", "Neo4j", "CouchDB", "InfluxDB", "TimescaleDB",
    
    # Cloud & DevOps
    "Docker", "Kubernetes", "AWS", "Azure", "Google Cloud", "Terraform", "Ansible", "Jenkins",
    "GitLab CI", "GitHub Actions", "Prometheus", "Grafana", "ELK Stack", "Vagrant", "Packer",
    "Helm", "Istio", "Consul", "Vault", "Nomad", "Rancher", "OpenShift", "CloudFormation",
    
    # Mobile Development
    "React Native", "Flutter", "Xamarin", "Ionic", "Cordova", "PhoneGap", "Swift", "Kotlin",
    "Android Studio", "Xcode", "App Store", "Google Play", "Firebase", "Crashlytics",
    
    # Data Science & AI
    "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Keras", "Scikit-learn",
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Jupyter", "Apache Spark", "Hadoop",
    "Data Analysis", "Statistics", "R", "SAS", "SPSS", "Tableau", "Power BI", "Looker",
    "Natural Language Processing", "Computer Vision", "OpenCV", "NLTK", "spaCy", "BERT",
    "GPT", "Transformers", "MLops", "MLflow", "Kubeflow", "Weights & Biases",
    
    # Testing
    "Unit Testing", "Integration Testing", "Selenium", "Cypress", "Jest", "Mocha", "Chai",
    "Pytest", "JUnit", "TestNG", "Cucumber", "SpecFlow", "Postman", "Newman", "JMeter",
    "Load Testing", "Performance Testing", "Security Testing", "Penetration Testing",
    
    # Security
    "Cybersecurity", "OWASP", "Penetration Testing", "Ethical Hacking", "Network Security",
    "Application Security", "Data Security", "Cryptography", "SSL/TLS", "OAuth", "JWT",
    "SAML", "LDAP", "Active Directory", "Firewall", "VPN", "IDS/IPS", "SIEM", "SOC",
    
    # Project Management
    "Agile", "Scrum", "Kanban", "Jira", "Confluence", "Trello", "Asana", "Monday.com",
    "Project Management", "Product Management", "Business Analysis", "Requirements Analysis",
    "User Stories", "Sprint Planning", "Retrospectives", "SAFe", "Lean", "Six Sigma",
    
    # Design & UX
    "UI/UX Design", "Figma", "Sketch", "Adobe XD", "InVision", "Zeplin", "Principle",
    "Framer", "Adobe Photoshop", "Adobe Illustrator", "Adobe After Effects", "Blender",
    "3D Modeling", "Prototyping", "Wireframing", "User Research", "Usability Testing",
    
    # Communication & Soft Skills
    "Communication", "Leadership", "Team Management", "Problem Solving", "Critical Thinking",
    "Time Management", "Project Coordination", "Stakeholder Management", "Presentation Skills",
    "Technical Writing", "Documentation", "Mentoring", "Training", "Public Speaking",
    
    # Version Control & Tools
    "Git", "GitHub", "GitLab", "Bitbucket", "SVN", "Mercurial", "Perforce", "TFS",
    "VS Code", "IntelliJ IDEA", "Eclipse", "Sublime Text", "Vim", "Emacs", "Atom",
    
    # Operating Systems
    "Linux", "Ubuntu", "CentOS", "Red Hat", "Debian", "Windows Server", "macOS",
    "Unix", "FreeBSD", "OpenBSD", "Solaris", "AIX", "HP-UX", "System Administration",
    
    # Networking
    "TCP/IP", "HTTP/HTTPS", "REST API", "GraphQL", "WebSocket", "gRPC", "Microservices",
    "Load Balancing", "CDN", "DNS", "DHCP", "VPN", "Firewall", "Network Protocols",
    
    # Frameworks & Libraries
    "Spring", "Hibernate", "MyBatis", "Struts", "JSF", "PrimeFaces", "Vaadin",
    "Play Framework", "Akka", "Apache Kafka", "RabbitMQ", "Apache ActiveMQ", "ZeroMQ",
    "Apache Camel", "Spring Integration", "Spring Security", "Spring Data", "Spring Cloud",
    
    # Other Technologies
    "Blockchain", "Smart Contracts", "Solidity", "Web3", "Ethereum", "Bitcoin", "Cryptocurrency",
    "IoT", "Arduino", "Raspberry Pi", "Embedded Systems", "Firmware", "Device Drivers",
    "Game Development", "Unity", "Unreal Engine", "Cocos2d", "Godot", "Blender",
    "AR/VR", "Augmented Reality", "Virtual Reality", "Mixed Reality", "Oculus", "HTC Vive"
]
