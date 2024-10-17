import os
import json
from dotenv import load_dotenv
from services.bedrockService import generate_care_procedures

# Carrega variáveis de ambiente
load_dotenv()

def generateCareProcedures(event, context):
    try:
        # Extrai o texto e o contexto do evento
        text = event.get('text', '')
        context = event.get('context', 'tips')

        # Verifica se o texto está vazio
        if not text:
            return {
                'statusCode': 400,
                'body': json.dumps('Texto para análise é obrigatório.')
            }

        # Chama a função generate_care_procedures do bedrockService
        care_procedures = generate_care_procedures(text, context)

        # Retorna a resposta da função generate_care_procedures
        return {
            'statusCode': 200,
            'body': json.dumps(care_procedures)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Erro ao gerar procedimentos de cuidados: {str(e)}')
        }
