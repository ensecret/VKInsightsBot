#config.py
import os
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Получение токенов из переменных окружения
VK_TOKEN = os.getenv('VK_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

# Чтение Chat ID из файла
try:
    with open("chat_id.txt", "r", encoding='utf-8') as f:
        TELEGRAM_CHAT_ID = f.read().strip()
except FileNotFoundError:
    TELEGRAM_CHAT_ID = None
    print("Файл chat_id.txt не найден. Пожалуйста, сначала запустите get_chat_id.py и получите Chat ID.")

# Другие конфигурации
SEARCH_QUERY = 'подписывайтесь на мой канал на ютуб'
CHECK_INTERVAL = 1  # Уменьшение интервала для тестирования
LOG_FILE = 'bot.log'