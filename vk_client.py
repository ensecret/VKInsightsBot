# vk_client.py
import vk_api
import logging
from datetime import datetime, timedelta

from config import VK_TOKEN

# Инициализация VK
vk_session = vk_api.VkApi(token=VK_TOKEN)
vk = vk_session.get_api()

def is_page_active(owner_id):
    try:
        if owner_id > 0:
            response = vk.users.get(user_ids=owner_id, fields='last_seen')
            last_seen = response[0].get('last_seen', {}).get('time')
            if last_seen:
                last_active = datetime.fromtimestamp(last_seen)
                return (datetime.now() - last_active) < timedelta(days=30)
            return False
        else:
            group_id = -owner_id
            response = vk.groups.getById(group_id=group_id, fields='activity')
            activity = response[0].get('activity')
            return activity is not None
    except Exception as e:
        logging.error(f"Ошибка при проверке активности страницы {owner_id}: {e}")
        return False

def search_posts(query, years=5):
    items = []
    now = datetime.now()
    for i in range(years):
        start_date = datetime(now.year - i, 1, 1)
        end_date = datetime(now.year - i, 12, 31, 23, 59, 59)
        start_timestamp = int(start_date.timestamp())
        end_timestamp = int(end_date.timestamp())
        logging.info(f"Поиск постов с {start_date.strftime('%Y-%m-%d %H:%M:%S')} до {end_date.strftime('%Y-%m-%d %H:%M:%S')}")
        try:
            response = vk.newsfeed.search(q=query, count=100, extended=1, start_time=start_timestamp, end_time=end_timestamp)
            items.extend(response.get('items', []))
        except Exception as e:
            logging.error(f"Ошибка при поиске постов: {e}")
    return items