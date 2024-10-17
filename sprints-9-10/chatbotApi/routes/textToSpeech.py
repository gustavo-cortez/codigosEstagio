import os
import json
import boto3
from services.dynamodbService import generate_hash, save_to_dynamo, create_table_if_not_exists, check_text_in_dynamo
from services.s3BucketService import upload_to_s3
from services.pollyService import synthesize_speech
from utils.audioUtils import success_response
from dotenv import load_dotenv
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

# Carrega variáveis de ambiente
load_dotenv()

# Inicializa o cliente lambda
lambda_client = boto3.client('lambda')

def textToSpeech(event, context):
    bucket_name = os.getenv('AUDIO_BUCKET_NAME')
    table_name = os.getenv('AUDIO_TABLE_NAME')
    create_table_if_not_exists(table_name)

    # Verifica se o evento veio como uma string JSON encapsulada
    if 'body' in event:
        data = json.loads(event['body'])
        text = data.get('text')
    else:
        text = event.get('text')

    if not text:
        return {"statusCode": 400, "body": json.dumps({"error": "Text not provided"})}

    # Cria um hash único para o texto
    unique_id = generate_hash(text)

    # Verifica se a frase já existe no DynamoDB
    existing_record = check_text_in_dynamo(unique_id, table_name)

    if existing_record:
        return success_response(text, existing_record)

    # Gera o áudio usando o serviço AWS Polly
    audio_stream = synthesize_speech(text)

    # Salva o áudio em um arquivo temporário
    audio_file = f"/tmp/{unique_id}.mp3"
    if audio_stream:
        with open(audio_file, 'wb') as file:
            file.write(audio_stream)

    # Define a chave do S3 para ser o nome do arquivo diretamente na raiz do bucket
    s3_key = f"Audios/{unique_id}.mp3"

    # Faz upload do arquivo para o S3
    s3_url = upload_to_s3(audio_file, bucket_name, s3_key)

    # Salva os detalhes do áudio no DynamoDB
    created_audio = datetime.now(ZoneInfo("America/Sao_Paulo")).strftime('%Y-%m-%d %H:%M:%S')
    item = {
        'unique_id': unique_id,
        'received_phrase': text,
        'url_to_audio': s3_url,
        'created_audio': created_audio
    }
    save_to_dynamo(item, table_name)

    # Retorna os detalhes do áudio criado
    return success_response(text, item)
