import json
import boto3
from utils.sendMessageUtils import send_to_telegram, send_audio_to_telegram
from lambdaInvoker import invoke_lambda_tts

# Configura cliente lambda
lambda_client = boto3.client('lambda')

# Modelo de resposta de sucesso para áudio armazenado
def success_response(text, record):
    return {
        "statusCode": 200,
        "body": json.dumps({
            'received_text': text,
            'url_to_audio': record['url_to_audio'],
            'created_audio': record['created_audio'],
            'unique_id': record['unique_id']
        })
    }

# Combina textos do lex e gera um único áudio
def combine_texts_and_generate_audio(messages_for_telegram, chat_id):
    combined_text = ""

    for message in messages_for_telegram:
        send_to_telegram(message)

        if 'text' in message and message['text']:
            combined_text += message['text'] + " "

        if message.get('reply_markup'):
            buttons = message['reply_markup'].inline_keyboard
            for row in buttons:
                for button in row:
                    combined_text += button.text + " "

    if combined_text:
        audio_url = invoke_lambda_tts(combined_text.strip())
        send_audio_to_telegram(chat_id, audio_url)

