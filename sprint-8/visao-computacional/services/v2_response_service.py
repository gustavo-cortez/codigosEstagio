from datetime import datetime
from utils.image_utils import format_image_url
from utils.generate_tips import generate_tips

# Organiza a resposta no formato especificado
def generate_response_body_v2(bucket, imageName, faces, labels=None):
    created_image = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Inicializa a estrutura de resposta básica da resposta(com e sem faces)
    if faces:
        response_body = {
            "url_to_image": format_image_url(bucket, imageName),
            "created_image": created_image,
            "faces": [],
            "pets": []
        }
    else:
        response_body = {
            "url_to_image": format_image_url(bucket, imageName),
            "created_image": created_image,
            "pets": []
        }

    # Processa as informações de rostos se houver
    if faces:
        for face in faces:
            # Identifica a emoção predominante no rosto
            emotion = max(face['Emotions'], key=lambda x: x['Confidence'])
            response_body['faces'].append({
                "position": face['BoundingBox'],
                "classified_emotion": emotion['Type'],
                "classified_emotion_confidence": round(emotion['Confidence'], 2)
            })

    # Lista de rótulos de animais e rótulos proibidos 
    animal_labels = ['Dog', 'Cat', 'Bird', 'Fish', 'Reptile', 'Amphibian']
    proibido_labels = ['Mammal', 'Canine', 'Puppy', 'Kitten', 'Animal', 'Dog', 'Cat']
    
    # Conjunto para rastrear nomes de raças de animais já adicionados
    breed_labels = set()

    # Itera sobre os rótulos fornecidos
    for label in labels:
        if label['Name'] in animal_labels:
            pet_info = {}
            pet_info['labels'] = []
            # Determina que é um animal
            pet_info['labels'].append({
                "Confidence": label['Confidence'],
                "Name": 'Animal'
            })
            # Determina a espécie do animal
            pet_info['labels'].append({
                "Confidence": label['Confidence'],
                "Name": label['Name']
            })
            # Determina se animal é um pet ou não percorrendo as labels geradas 
            # pelo Rekognition e aplicando filtros com base nos "pais" dessa labe
            for instance in labels:
                if instance['Name'] not in proibido_labels and 'Parents' in instance and 'Animal' in [parent['Name'] for parent in instance['Parents']] and not 'Dog' in [parent['Name'] for parent in instance['Parents']] and not 'Cat' in [parent['Name'] for parent in instance['Parents']]:
                    pet_info['labels'].append({
                        "Confidence": instance['Confidence'],
                        "Name": instance['Name']
                    })
                    break

            # Determina a raça do animal identificado percorrendo as labels geradas 
            # pelo Rekognition e aplicando filtros com base nos "pais" dessa label
            for instance in labels:
                if instance['Name'] not in proibido_labels and 'Parents' in instance and label['Name'] in [parent['Name'] for parent in instance['Parents']]:
                    if instance['Name'] not in breed_labels:
                        pet_info['labels'].append({
                            "Confidence": instance['Confidence'],
                            "Name": instance['Name']
                        })
                        breed_labels.add(instance['Name'])
                        break

            # Obtendo dicas de acordo com a raça do animal
            if len(pet_info['labels']) >= 4:
                breed_label = pet_info['labels'][3] # Obtém o rótulo da raça do animal
                animal_label = pet_info['labels'][1] # Obtém o rótulo do tipo de animal
                breed_name = breed_label['Name']
                animal_name = animal_label['Name']
                tips = generate_tips(breed_name, animal_name) # Gera dicas com base na raça e tipo de animal
                
                # Adiciona as dicas diretamente no objeto pet_info
                pet_info['Dicas'] = tips

            # Adiciona as informações do animal à lista de animais na resposta
            response_body['pets'].append(pet_info) 

    if not labels:
        pet_info = {}
        pet_info['labels'] = []
        pet_info['labels'].append({
            "Confidence": 'None',
            "Name": 'None'
        })
        pet_info['labels'].append({
            "Confidence": 'None',
            "Name": 'None'
        })
        response_body['pets'].append(pet_info)

    return response_body