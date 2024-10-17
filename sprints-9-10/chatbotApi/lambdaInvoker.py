import json
import boto3

# Inicializa o cliente Lambda
lambda_client = boto3.client('lambda')

# Invoca a lambda generateTips para gerar dicas sobre pets
def invoke_lambda_generate_tips(text, context):
    try:
        response = lambda_client.invoke(
            FunctionName='chatbot-api-dev-generateTips',
            InvocationType='RequestResponse',
            Payload=json.dumps({
                'text': text,
                'context': context
            })
        )
        response_payload = json.loads(response['Payload'].read())
        return json.loads(response_payload['body'])
    except Exception as e:
        return f"Erro ao invocar Lambda: {str(e)}"

# Invoca a lambda analyzeImege para analisar imagem e detectar raça de animal identificado
def invoke_lambda_analyze_image(body):
    try:
        response = lambda_client.invoke(
            FunctionName='chatbot-api-dev-analyzeImage',
            InvocationType='RequestResponse',
            Payload=json.dumps(body)
        )
        response_payload = json.loads(response['Payload'].read())
        return json.loads(response_payload['body'])
    except Exception as e:
        return {
            'text': f"Erro ao invocar Lambda: {str(e)}",
            'chat_id': body.get('message', {}).get('chat', {}).get('id', None)
        }

# Invoca a lambda textToSpeech para converter texto em áudio
def invoke_lambda_tts(bot_message):
    try:
        # Prepara o payload para a função Lambda de TTS
        tts_payload = json.dumps({"text": bot_message})
        print("TTS Payload: ", tts_payload)
        
        # Invoca a função Lambda para gerar o áudio
        tts_response = lambda_client.invoke(
            FunctionName='chatbot-api-dev-textToSpeech',
            InvocationType='RequestResponse',
            Payload=tts_payload
        )
        
        # Lê e decodifica a resposta da função Lambda
        tts_response_payload = json.loads(tts_response['Payload'].read())
        print("TTS Response Status Code: ", tts_response_payload['statusCode'])
        print("TTS Response Body: ", tts_response_payload['body'])
        
        if tts_response_payload['statusCode'] == 200:
            tts_data = json.loads(tts_response_payload['body'])
            audio_url = tts_data.get('url_to_audio')
            print("Audio URL: ", audio_url)
            return audio_url
        else:
            print("Erro ao chamar a função Lambda de TTS: ", tts_response_payload['body'])
            return None
    except Exception as e:
        print("Exceção ao chamar a função Lambda de TTS: ", str(e))
        return None
