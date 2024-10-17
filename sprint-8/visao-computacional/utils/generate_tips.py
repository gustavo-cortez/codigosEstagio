from services.bedrock_service import invoke_bedrock
import json 

def generate_tips(breed, animal):
    try:
        # Cria um único prompt que inclui todas as perguntas
        prompt = (
            f"Sobre {animal} da raça {breed} retorne dicas exatamente no formato abaixo:\n"
            f"Nível de Energia e Necessidades de Exercícios:\n"
            f"Temperamento e Comportamento:\n"
            f"Cuidados e Necessidades:\n"
            f"Problemas de Saúde Comuns:\n"
            f"Responda em pt-br e seja breve nas respostas."
        )

        # Faz uma única chamada ao invoke_bedrock
        response = invoke_bedrock(prompt)

        # Processa a resposta JSON
        response_json = json.loads(response)
        output_text = response_json.get("outputText", "")

        output_text = output_text.replace("\n", "").strip()

        # Adiciona o prefixo desejado
        tips_with_prefix = f"Dicas sobre {breed}: {output_text}"

        return tips_with_prefix

    except Exception as e:
        print(f"Erro ao obter dicas para a raça {breed}: {e}")
        return json.dumps({
            'statusCode': 500,
            'body': 'Erro ao obter dicas para esta raça.'
        })
