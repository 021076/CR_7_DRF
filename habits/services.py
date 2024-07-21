import requests
from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN


def telegram_sending(chat_id, message):
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage', params=params)