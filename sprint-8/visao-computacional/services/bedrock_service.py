import boto3
import json

# Cria conexão com Bedrock
client = boto3.client('bedrock-runtime')

def invoke_bedrock(prompt):
    try:
        # Configuração do payload para a solicitação ao modelo Bedrock
        payload = {
            "inputText": prompt,
            "textGenerationConfig": {
                "temperature": 0.4,     # Valor menor diminui aleatoriedade
                "topP": 0.7,            # Valor menor ignora opções menos prováveis e diminui diversidade das respostas
                "maxTokenCount": 500    # Limitando a 500 tokens por prompt
            }
        }

        # Codifica o payload para bytes no formato UTF-8
        payload_bytes = json.dumps(payload).encode('utf-8')

        # Chama o modelo Bedrock usando o cliente configurado
        response = client.invoke_model(
            body=payload_bytes,
            contentType='application/json',
            accept='application/json',
            modelId='amazon.titan-text-express-v1'
        )

        # Lê a resposta como bytes, decodifica para string e carrega como JSON
        response_body_bytes = response['body'].read()
        response_body_str = response_body_bytes.decode('utf-8')
        response_body = json.loads(response_body_str)

        # Extrai os resultados da resposta, se houver
        results = response_body.get('results', [])

        if results:
            # Extrai o texto de saída do primeiro resultado, ou define uma mensagem padrão se nenhum resultado for gerado
            output_text = results[0].get('outputText', 'Nenhuma resposta gerada')
            return json.dumps({"outputText": output_text})
        else:
            # Retorna uma mensagem padrão se nenhum resultado for retornado
            return json.dumps({"outputText": "Sem resultados gerados"})
        
    # Tratamento de erros
    except Exception as e:
        print(f"Erro ao obter dica sobre {prompt}: {e}")
        return json.dumps({
            'statusCode': 500,
            'body': 'Erro ao obter dica'
        })