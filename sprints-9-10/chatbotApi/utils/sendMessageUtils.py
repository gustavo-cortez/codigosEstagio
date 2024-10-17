import requests
import json
import os
import boto3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

# Inicializa os clientes do Amazon Lex V2 e S3
lexruntimev2 = boto3.client('lexv2-runtime')
s3_client = boto3.client('s3')

# Carrega variáveis de ambiente
load_dotenv()

# Envia uma mensagem de texto para o chat do Telegram
def send_to_telegram(message):
    token = os.getenv('TELEGRAM_TOKEN')
    telegram_url = f'https://api.telegram.org/bot{token}/sendMessage'

    payload = {
        'chat_id': message['chat_id'],
        'text': message['text']
    }

    if message.get('reply_markup'):
        payload['reply_markup'] = json.dumps(message['reply_markup'].to_dict())

    print("Payload to Telegram:", payload)
    response = requests.post(telegram_url, json=payload)
    return response.json()

# Baixa o áudio a partir do URL
def download_audio(audio_url):
    response = requests.get(audio_url)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"Failed to download audio: {response.status_code}")

# Envia um áudio para o chat do Telegram
def send_audio_to_telegram(chat_id, audio_url):
    token = os.getenv('TELEGRAM_TOKEN')
    telegram_url = f'https://api.telegram.org/bot{token}/sendAudio'
    title = 'Clique para ouvir!'

    # Baixa o áudio do URL
    audio_data = download_audio(audio_url)

    # Prepara os arquivos e dados para envio
    files = {
        'audio': ('audio.mp3', audio_data)
    }
    data = {
        'chat_id': chat_id,
        'title': title,
    }

    print("Enviando payload para Telegram:", data)
    response = requests.post(telegram_url, files=files, data=data)
    print("Resposta do Telegram:", response.json())
    return response.json()


# Envia uma foto para o chat do Telegram
def send_photo_to_telegram(photo_data):
    token = os.getenv('TELEGRAM_TOKEN')
    telegram_url = f'https://api.telegram.org/bot{token}/sendPhoto'
    print("Photo Payload to Telegram:", photo_data)
    response = requests.post(telegram_url, json=photo_data)
    return response.json()

# Envia uma lista de imagens para o chat do Telegram com um botão para solicitar mais fotos
def send_images(chat_id, images, species):
    # Inicializa o contador para numerar os animais
    animal_counter = 1
    
    for image_url in images:
        # Criar o caption conforme a espécie e o número do animal
        caption = f'{species.capitalize()} disponível para adoção {animal_counter}. Caso queria dar uma lar a esse bichinho salve a foto dele e mande para o número 67 1234-5678 com a mensagem "Quero adotar!"'
        
        photo_data = {
            'chat_id': chat_id,
            'photo': image_url,
            'caption': caption
        }
        send_photo_to_telegram(photo_data)
        
        # Incrementa o contador para a próxima imagem
        animal_counter += 1

    # Enviar mensagem com informações de contato
    contact_message = {
        'chat_id': chat_id,
        'text': 'Caso você deseje adotar algum pet, entre em contato no número 67 1234-5678 para dar início ao processo de adoção.'
    }
    send_to_telegram(contact_message)

    # Enviar botão para mais fotos
    more_photos_button = InlineKeyboardButton('Mais fotos', callback_data=f'Mais fotos {species}')
    back_to_menu_button = InlineKeyboardButton('Voltar para menu', callback_data='Olá')
    reply_markup = InlineKeyboardMarkup([[more_photos_button, back_to_menu_button]])
    more_photos_message = {
        'chat_id': chat_id,
        'text': 'Deseja ver mais fotos?',
        'reply_markup': reply_markup
    }
    send_to_telegram(more_photos_message)
