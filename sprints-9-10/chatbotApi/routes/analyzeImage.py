import os
import json
from dotenv import load_dotenv
from services.rekognitionServices import handle_image

# Carrega variáveis de ambiente
load_dotenv()

def handleImage(event, context):
    try:
        response = handle_image(event)
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
