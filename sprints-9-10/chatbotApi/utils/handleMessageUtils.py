import os
import json
import boto3
from dotenv import load_dotenv
from utils.sendMessageUtils import send_to_telegram, send_audio_to_telegram
from services.rekognitionServices import handle_image
from session import user_session, response_mode
from lambdaInvoker import invoke_lambda_analyze_image, invoke_lambda_generate_tips, invoke_lambda_tts
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

# Carrega variáveis de ambiente
load_dotenv()

def handle_image_or_text(body, chat_id, is_photo=False):
    combined_text = ""

    if is_photo:
        if user_session.get(chat_id) == 'pet_tips':
            # Processar imagem para dicas de cuidados
            handle_pet_tips_request(body, chat_id)
        else:
            # Processar imagem para resgate
            response_message = invoke_lambda_analyze_image(body)
            send_to_telegram(response_message)

            combined_text += response_message['text'] + " "

            # Gerar recomendações de resgate com a Lambda
            care_procedures = invoke_lambda_generate_tips(response_message['text'], context='rescue')
            care_message = {
                'chat_id': chat_id,
                'text': f'Recomendações de cuidados: {care_procedures}'
            }
            send_to_telegram(care_message)

            combined_text += care_message['text'] + " "

            # Enviar link para formulário Google
            form_message = {
                'chat_id': chat_id,
                'text': 'Leve o animal até a ONG mais próxima ou preencha este formulário para que possamos buscar: https://forms.gle/3FeY6GZPQnyFeYGT6'
            }
            send_to_telegram(form_message)

            combined_text += form_message['text'] + " "

            # Enviar botão de voltar para menu
            back_to_menu_button = InlineKeyboardButton('Voltar para menu', callback_data='Olá')
            reply_markup = InlineKeyboardMarkup([[back_to_menu_button]])
            back_to_menu_message = {
                'chat_id': chat_id,
                'text': 'Se precisar de mais ajuda, clique no botão abaixo para voltar ao menu.',
                'reply_markup': reply_markup
            }
            send_to_telegram(back_to_menu_message)

            combined_text += back_to_menu_message['text'] + " "

    else:
        # Processar texto
        message_text = body['message']['text']
        care_procedures = invoke_lambda_generate_tips(message_text, context='rescue')
        care_message = {
            'chat_id': chat_id,
            'text': f'Recomendações de cuidados: {care_procedures}'
        }
        send_to_telegram(care_message)

        combined_text += care_message['text'] + " "

        # Enviar link para formulário Google
        form_message = {
            'chat_id': chat_id,
            'text': 'Leve o animal até a ONG mais próxima ou preencha este formulário para que possamos buscar: https://forms.gle/3FeY6GZPQnyFeYGT6'
        }
        send_to_telegram(form_message)

        combined_text += form_message['text'] + " "

        # Enviar botão de voltar para menu
        back_to_menu_button = InlineKeyboardButton('Voltar para menu', callback_data='Olá')
        reply_markup = InlineKeyboardMarkup([[back_to_menu_button]])
        back_to_menu_message = {
            'chat_id': chat_id,
            'text': 'Se precisar de mais ajuda, clique no botão abaixo para voltar ao menu.',
            'reply_markup': reply_markup
        }
        send_to_telegram(back_to_menu_message)

        combined_text += back_to_menu_message['text'] + " "

    # Gera áudio combinado e envia
    print(f"Response mode for chat_id {chat_id}: {response_mode.get(chat_id)}")
    if response_mode.get(chat_id) == 'Áudio':
        audio_url = invoke_lambda_tts(combined_text.strip())
        send_audio_to_telegram(chat_id, audio_url)

def handle_pet_tips_request(body, chat_id):
    # Inicializa variável para combinar texto
    combined_text = ""

    if 'photo' in body['message']:
        # Processar imagem
        response_message = invoke_lambda_analyze_image(body)
        send_to_telegram(response_message)
        
        combined_text += response_message['text'] + " "

        # Gerar recomendações de cuidados com a Lambda
        care_procedures = invoke_lambda_generate_tips(response_message['text'], context='tips')
        care_message = {
            'chat_id': chat_id,
            'text': f'Recomendações de cuidados: {care_procedures}'
        }
        send_to_telegram(care_message)
        
        combined_text += care_message['text'] + " "

        # Enviar mensagem final somente se dicas forem encontradas
        if "Nenhum animal identificado" not in response_message['text']:
            final_message = {
                'chat_id': chat_id,
                'text': 'Espero que essas dicas sejam úteis, lembre-se que é essencial levar seu pet ao veterinário regularmente para garantir que ele esteja saudável e recebendo os cuidados adequados.'
            }
            send_to_telegram(final_message)
            
            combined_text += final_message['text'] + " "

        # Enviar botão de voltar para menu
        back_to_menu_button = InlineKeyboardButton('Voltar para menu', callback_data='Olá')
        reply_markup = InlineKeyboardMarkup([[back_to_menu_button]])
        back_to_menu_message = {
            'chat_id': chat_id,
            'text': 'Se quiser utilizar o serviço novamente, clique no botão abaixo para voltar ao menu.',
            'reply_markup': reply_markup
        }
        send_to_telegram(back_to_menu_message)
        
        combined_text += back_to_menu_message['text'] + " "

        # Gera áudio combinado e envia
    print(f"Response mode for chat_id {chat_id}: {response_mode.get(chat_id)}")
    if response_mode.get(chat_id) == 'Áudio':
        audio_url = invoke_lambda_tts(combined_text.strip())
        send_audio_to_telegram(chat_id, audio_url)

    elif 'text' in body['message']:
        # Processar texto
        message_text = body['message']['text']
        care_procedures = invoke_lambda_generate_tips(message_text, context='tips')
        care_message = {
            'chat_id': chat_id,
            'text': f'Recomendações de cuidados: {care_procedures}'
        }
        send_to_telegram(care_message)
        
        combined_text += care_message['text'] + " "

        # Enviar mensagem final somente se dicas forem encontradas
        if "Nenhum animal identificado" not in message_text:
            final_message = {
                'chat_id': chat_id,
                'text': 'Espero que essas dicas sejam úteis, mas lembre-se também que é essencial levar seu pet ao veterinário regularmente para garantir que ele esteja saudável e recebendo os cuidados adequados.'
            }
            send_to_telegram(final_message)
            
            combined_text += final_message['text'] + " "

        # Enviar botão de voltar para menu
        back_to_menu_button = InlineKeyboardButton('Voltar para menu', callback_data='Olá')
        reply_markup = InlineKeyboardMarkup([[back_to_menu_button]])
        back_to_menu_message = {
            'chat_id': chat_id,
            'text': 'Se quiser utilizar o serviço novamente, clique no botão abaixo para voltar ao menu.',
            'reply_markup': reply_markup
        }
        send_to_telegram(back_to_menu_message)
        
        combined_text += back_to_menu_message['text'] + " "

    # Gera áudio combinado e envia
    print(f"Response mode for chat_id {chat_id}: {response_mode.get(chat_id)}")
    if response_mode.get(chat_id) == 'Áudio':
        audio_url = invoke_lambda_tts(combined_text.strip())
        send_audio_to_telegram(chat_id, audio_url)