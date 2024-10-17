import boto3
import json
import requests
from utils.telegramUtils import *

# Inicializa o cliente do Amazon Rekognition
rekognition = boto3.client('rekognition')

def handle_image(body):
    # Processa uma imagem recebida do Telegram para identificar animais usando o Amazon Rekognition
    try:
        # Obtém o ID do arquivo da foto enviada
        file_id = body['message']['photo'][-1]['file_id']
        # Obtém o caminho do arquivo usando o ID
        file_path = get_telegram_file_path(file_id)
        # Baixa a imagem do Telegram
        image_bytes = download_image(file_path)

        # Detecta labels na imagem usando Amazon Rekognition
        rekognition_response = rekognition.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=10,
            MinConfidence=75
        )

        # Extrai os nomes das labels e converte para minúsculas
        labels = [label['Name'].lower() for label in rekognition_response['Labels']]
        # Detecta raças de animais baseadas nas labels
        animal_breeds = detect_animal_breeds(labels)

        # Cria a mensagem com os animais identificados ou uma mensagem padrão se nenhum animal for encontrado
        if animal_breeds:
            labels_message = f"\nAnimais identificados: {', '.join(animal_breeds)}"
        else:
            labels_message = "Nenhum animal identificado."

        return {
            'text': labels_message,
            'chat_id': body['message']['chat']['id']
        }

    except KeyError as e:
        # Trata erros de chave ausente
        print(f"KeyError in handle_image: {str(e)}")
        return {
            'text': 'Não foi possível processar a imagem. Chave ausente: ' + str(e),
            'chat_id': body['message']['chat']['id']
        }
    except Exception as e:
        # Trata outros erros
        print(f'Error in handle_image: {str(e)}')
        return {
            'text': 'Não foi possível processar a imagem. Por favor, tente novamente.',
            'chat_id': body['message']['chat']['id']
        }

def detect_animal_breeds(labels):
    # Detecta raças de animais com base nas labels fornecidas
    animal_breeds = set()  # Usar um conjunto para evitar duplicatas
    # Mapeia labels detectadas para raças de animais
    animal_mapping = {
        'cachorro': ['dog', 'puppy'],
        'gato': ['cat', 'kitten'],
        'cavalo': ['horse', 'pony'],
    }

    # Verifica se cada label corresponde a uma raça de animal
    for label in labels:
        for animal, breeds in animal_mapping.items():
            if any(breed in label for breed in breeds):
                animal_breeds.add(animal.capitalize())
                break

    return list(animal_breeds)  # Converte o conjunto de volta para uma lista

def analyze_image(image_url):
    # Analisa uma imagem a partir de uma URL para identificar labels usando o Amazon Rekognition
    # Baixa a imagem a partir da URL
    response = requests.get(image_url)
    image_bytes = response.content

    # Detecta labels na imagem usando Amazon Rekognition
    rekognition_response = rekognition.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=75
    )

    # Extrai os nomes das labels
    labels = [label['Name'] for label in rekognition_response['Labels']]
    return labels
