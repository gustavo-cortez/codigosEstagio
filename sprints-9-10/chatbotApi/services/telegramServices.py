import os
import boto3
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
from utils.audioUtils import combine_texts_and_generate_audio
from services.s3BucketService import get_animal_images
from utils.sendMessageUtils import send_images, send_to_telegram
from utils.sendMessageUtils import send_to_telegram, send_images
from session import user_session, response_mode
from utils.sendMessageUtils import send_audio_to_telegram
from utils.audioUtils import invoke_lambda_tts

# Inicializa os clientes do Amazon Lex V2 e S3
lexruntimev2 = boto3.client('lexv2-runtime')
s3_client = boto3.client('s3')

# Carrega variáveis de ambiente
load_dotenv()

def map_telegram_to_lex(body):
    chat_id = str(body['message']['chat']['id'])
    message = body['message']['text']
    return {
        'inputText': message,
        'userId': chat_id,
        'sessionAttributes': {}
    }

def map_lex_to_telegram(lex_response, body):
    chat_id = body['message']['chat']['id']
    messages = []

    if 'messages' in lex_response:
        for lex_message in lex_response['messages']:
            message = {
                'chat_id': chat_id,
                'text': None,
                'reply_markup': None
            }

            if 'imageResponseCard' in lex_message:
                response_card = lex_message['imageResponseCard']
                print("Lex response card:", response_card)

                buttons = []
                if 'buttons' in response_card:
                    for button in response_card['buttons']:
                        buttons.append(InlineKeyboardButton(button['text'], callback_data=button['value']))

                if buttons:
                    message['reply_markup'] = InlineKeyboardMarkup.from_column(buttons)
                    message['text'] = response_card.get('title', 'Menu de opções')

                if message['reply_markup']:
                    messages.append(message)
            else:
                message['text'] = lex_message.get('content', 'Desculpe, não entendi sua mensagem.')
                messages.append(message)

    return messages

def recognize_text_with_lex(session_id, text):
    return lexruntimev2.recognize_text(
        botId=os.getenv('LEX_BOT_ID'),
        botAliasId=os.getenv('LEX_BOT_ALIAS_ID'),
        localeId='pt_BR',
        sessionId=session_id,
        text=text
    )

def process_lex_response(body, session_id, text):
    lex_response = recognize_text_with_lex(session_id, text)
    print("Lex response:", lex_response)
    messages_for_telegram = map_lex_to_telegram(lex_response, body)
    if response_mode.get(session_id) == 'Áudio':
        combine_texts_and_generate_audio(messages_for_telegram, body['message']['chat']['id'])
    else:    
        for message in messages_for_telegram:
            send_to_telegram(message)


def handle_callback_query(callback_query, chat_id, callback_data):
    if 'Mais fotos' in callback_data:
        species = callback_data.split(' ')[2]
        images = get_animal_images(species)
        send_images(chat_id, images, species)
    elif callback_data in ['Desejo adotar um gato', 'Desejo adotar um cachorro']:
        species = 'Gato' if 'gato' in callback_data.lower() else 'Cachorro'
        images = get_animal_images(species)
        send_images(chat_id, images, species)
    else:
        if callback_data == 'Desejo o serviço de resgate':
            resposta = "Por favor, envie uma foto do animal resgatado ou descreva a situação do animal."
            send_to_telegram({
                'chat_id': chat_id,
                'text': resposta
            })
            user_session[chat_id] = 'rescue'
            if response_mode.get(chat_id) == 'Áudio':
                audio_url = invoke_lambda_tts(resposta)
                send_audio_to_telegram(chat_id, audio_url)
        elif callback_data == 'Quero dicas sobre meu pet':
            resposta = "Por favor, envie uma foto do seu pet para que eu possa te dar dicas"
            send_to_telegram({
                'chat_id': chat_id,
                'text': resposta
            })
            user_session[chat_id] = 'pet_tips'
            if response_mode.get(chat_id) == 'Áudio':
                audio_url = invoke_lambda_tts(resposta)
                send_audio_to_telegram(chat_id, audio_url)
        elif callback_data.lower() == 'texto':
            send_to_telegram({
                'chat_id': chat_id,
                'text': 'Com essa opção eu te responderei apenas com textos 📖. Para voltar ao menu principal apenas digite um "Olá".'
            })
            response_mode[chat_id] = 'Texto'
        elif callback_data.lower() in ['áudio', 'audio']:
            resposta = 'Com essa opção eu te responderei com áudios e textos 🔊. Para voltar ao menu principal apenas digite um "Olá".'
            send_to_telegram({
                'chat_id': chat_id,
                'text': resposta
            })
            audio_url = invoke_lambda_tts(resposta)
            response_mode[chat_id] = 'Áudio'
            print(f"Response mode for chat_id {chat_id}: {response_mode.get(chat_id)}")
            send_audio_to_telegram(chat_id, audio_url)
        else:
            process_lex_response(callback_query, chat_id, callback_data)


