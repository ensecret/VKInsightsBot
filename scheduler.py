# scheduler.py
import schedule
import asyncio
import logging
from datetime import datetime

from config import CHECK_INTERVAL, SEARCH_QUERY, TELEGRAM_CHAT_ID
from vk_client import search_posts, is_page_active
from telegram_client import send_message
from utils import load_sent_posts, save_sent_post

async def job():
    logging.info(f"Запуск поиска: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    await search_and_send_posts()

async def search_and_send_posts():
    logging.info("Выполняется поиск постов...")
    try:
        sent_posts = load_sent_posts("sent_posts.txt")

        items = search_posts(SEARCH_QUERY)
        logging.info(f"Найдено постов: {len(items)}")

        for item in items:
            post_id = item.get('id')
            owner_id = item.get('owner_id')
            unique_id = f"{owner_id}_{post_id}"
            date = datetime.fromtimestamp(item.get('date'))

            # Проверка активности страницы
            if not is_page_active(owner_id):
                logging.info(f"Страница {owner_id} неактивна. Пропуск.")
                continue

            # Проверка, был ли пост уже отправлен
            if unique_id in sent_posts:
                logging.info(f"Пост {unique_id} уже отправлен. Пропуск.")
                continue

            # Формирование ссылки на профиль
            if owner_id > 0:
                profile_url = f"https://vk.com/id{owner_id}"
            else:
                profile_url = f"https://vk.com/club{-owner_id}"

            # Формирование сообщения
            post_url = f"https://vk.com/wall{owner_id}_{post_id}"
            message = (
                f"Найдена публикация:\n{post_url}\n"
                f"Профиль автора: {profile_url}\n"
                f"Дата: {date.strftime('%Y-%m-%d %H:%M:%S')}"  # Исправлено: заменена "М" на "M" и добавлена секунда ":%S"
            )

            # Отправка в Telegram
            await send_message(TELEGRAM_CHAT_ID, message)
            save_sent_post("sent_posts.txt", unique_id)

    except Exception as e:
        logging.error(f"Ошибка при поиске постов: {e}")

def setup_scheduler():
    schedule.every(CHECK_INTERVAL).minutes.do(lambda: asyncio.create_task(job()))
    logging.info("Планировщик задач запущен.")