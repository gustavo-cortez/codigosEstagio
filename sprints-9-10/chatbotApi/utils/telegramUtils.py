import os
import requests
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

def get_telegram_file_path(file_id):
    token = os.getenv('TELEGRAM_TOKEN')
    file_url = f'https://api.telegram.org/bot{token}/getFile?file_id={file_id}'
    response = requests.get(file_url)
    file_path = response.json().get('result', {}).get('file_path')
    if not file_path:
        raise KeyError('file_path')
    return f'https://api.telegram.org/file/bot{token}/{file_path}'

def download_image(file_path):
    response = requests.get(file_path)
    return response.content

