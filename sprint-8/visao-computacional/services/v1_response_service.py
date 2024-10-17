from datetime import datetime
from utils.image_utils import format_image_url
from utils.face_utils import add_null_face
import boto3

# Organiza a resposta no formato especificado
def generate_response_body_v1(bucket, imageName, faces, labels=None):
    created_image = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    response_body = {
        "url_to_image": format_image_url(bucket, imageName),
        "created_image": created_image,
        "faces": [],
    }
    # Se não tiver faces, define como nulo
    if not faces:
        add_null_face(response_body['faces'])
    else:
        # Se tiver uma ou mais, itera sobre elas e retorna os detalhes
        for face in faces:
            emotion = max(face['Emotions'], key=lambda x: x['Confidence'])
            response_body['faces'].append({
                "position": face['BoundingBox'],
                "classified_emotion": emotion['Type'],
                "classified_emotion_confidence": round(emotion['Confidence'], 2)
            })

    return response_body
