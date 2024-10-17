import os
import json
import boto3
from services.telegramServices import handle_callback_query, map_telegram_to_lex, process_lex_response
from utils.handleMessageUtils import handle_image_or_text
from dotenv import load_dotenv

# Inicializa o cliente do Amazon Lex V2 e S3
lexruntimev2 = boto3.client('lexv2-runtime')
s3_client = boto3.client('s3')

# Carrega variáveis de ambiente
load_dotenv()

def telegramToLex(event, context):
    try:
        body = json.loads(event['body'])
        print('body:', body)

        if 'callback_query' in body:
            callback_query = body['callback_query']
            chat_id = callback_query['message']['chat']['id']
            callback_data = callback_query['data']
            handle_callback_query(callback_query, str(chat_id), callback_data)
        else:
            message = body['message']
            chat_id = str(message['chat']['id'])

            if 'photo' in message:
                handle_image_or_text(body, chat_id, is_photo=True)
            else:
                message_for_lex = map_telegram_to_lex(body)
                process_lex_response(body, message_for_lex['userId'], message_for_lex['inputText'])

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully processed message')
        }

    except Exception as e:
        print('Error in try catch:', str(e))
        return {
            'statusCode': 400,
            'body': json.dumps('Failed to process message')
        }
