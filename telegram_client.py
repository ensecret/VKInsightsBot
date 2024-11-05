#telegram_client.py
import telegram
import logging

from config import TELEGRAM_TOKEN

# Инициализация Telegram бота
bot = telegram.Bot(token=TELEGRAM_TOKEN)

async def send_message(chat_id, text):
    try:
        await bot.send_message(chat_id=chat_id, text=text)
        logging.info(f"Отправлено сообщение: {text}")
    except Exception as e:
        logging.error(f"Ошибка при отправке сообщения в Telegram: {e}")