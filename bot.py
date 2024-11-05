# main.py
import logging
import asyncio
import schedule  # Импорт модуля schedule
from scheduler import setup_scheduler
from telegram_client import send_message
from config import TELEGRAM_CHAT_ID, LOG_FILE

# Настройка логирования
handler = logging.FileHandler(LOG_FILE, encoding='utf-8')  # Установка кодировки
logging.basicConfig(
    handlers=[handler],
    level=logging.INFO,
    format='%(asctime)s - %(levelness)s - %(message)s'  # Исправлено с 'levellevel' на 'levelname'
)


async def main():
    if TELEGRAM_CHAT_ID is None:
        logging.error("Chat ID не найден. Пожалуйста, сначала запустите get_chat_id.py и получите Chat ID.")
        return

    # Отправка тестового сообщения
    await send_message(TELEGRAM_CHAT_ID, "Бот запущен и работает.")
    logging.info("Тестовое сообщение отправлено в Telegram.")

    # Настройка планировщика задач
    setup_scheduler()

    while True:
        schedule.run_pending()
        await asyncio.sleep(1)


# Запуск основной функции
asyncio.run(main())