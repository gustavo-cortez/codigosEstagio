import json
import boto3
import unicodedata

# Inicializa o cliente Bedrock
bedrock = boto3.client('bedrock-runtime')

def generate_care_procedures(text, context='tips'):
    # Verifica se o texto contém informações relevantes sobre um animal
    if not text or "Nenhum animal identificado" in text:
        return "Nenhum pet foi identificado. Não há dicas a serem geradas."

    # Prompt para dicas gerais
    if context == 'tips':
        prompt = (
            f"Gere a partir do texto a seguir sobre o animal identificado através de uma foto dicas de como cuidar, alimentação e atenções que deve-se tomar.\n"
            f"{text}\n"
            f"Responda em pt-br e seja breve nas respostas."
            f"Exemplo de resultado esperado: Alimente com ração de qualidade, ofereça água fresca, mantenha a caixa de areia limpa, visite o veterinário regularmente, forneça brinquedos e arranhadores, e dê carinho e atenção diária.\n"
        )
    # Prompt para dicas de resgate
    elif context == 'rescue':
        prompt = (
            f"A partir do texto a seguir sobre o animal identificado e que precisa ser resgatado, forneça orientações de primeiros socorros, cuidados imediatos e próximos passos para garantir a segurança e saúde do animal.\n"
            f"{text}\n"
            f"Responda em pt-br e seja breve nas respostas."
            f"Exemplo de resultado esperado: Mantenha o animal aquecido, ofereça água limpa e comida, limpe feridas com cuidado, leve ao veterinário imediatamente, forneça abrigo seguro e tranquilize o animal.\n"
        )
    else:
        raise ValueError("Contexto inválido. Use 'tips' ou 'rescue'.")

    payload = {
        "inputText": prompt,
        "textGenerationConfig": {
            "temperature": 0.5,
            "topP": 0.7,
            "maxTokenCount": 200
        }
    }

    payload_bytes = json.dumps(payload).encode('utf-8')

    bedrock_response = bedrock.invoke_model(
        body=payload_bytes,
        contentType='application/json',
        accept='application/json',
        modelId='amazon.titan-text-express-v1'
    )

    # Lê a resposta como bytes, decodifica para string e carrega como JSON
    response_body_bytes = bedrock_response['body'].read()
    response_body_str = response_body_bytes.decode('utf-8')
    response_body = json.loads(response_body_str)

    # Extrai os resultados da resposta, se houver
    results = response_body.get('results', [])

    if results:
        # Extrai o texto de saída do primeiro resultado
        output_text = results[0].get('outputText', 'Nenhuma resposta gerada')
        # Normaliza e limpa o texto de caracteres indesejados
        cleaned_text = unicodedata.normalize('NFKC', output_text)
        return cleaned_text
    else:
        # Retorna uma mensagem padrão se nenhum resultado for retornado
        return "Sem resultados gerados"
