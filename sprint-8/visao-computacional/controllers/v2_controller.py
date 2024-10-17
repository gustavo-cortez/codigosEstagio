import json
from services.rekognition_service import process_faces, process_labels
from services.v2_response_service import generate_response_body_v2

# Função para lidar com a rota de reconhecimento de faces e pets
def v2_vision_controller(event, context): #detecta animais 
    try:
        # Verifica se o corpo do evento está presente
        if 'body' not in event:
            raise ValueError("Missing body in event")
        
        # Extrai os campos do requerimento
        body = json.loads(event['body'])
        bucket = body.get('bucket')
        imageName = body.get('imageName')

        # Verifica se os campos necessários estão presentes
        if not bucket or not imageName:
            raise ValueError("Missing required fields: bucket or imageName")

        # Processa usando o serviço de Rekognition
        faces = process_faces(bucket, imageName)
        labels = process_labels(bucket, imageName)

        # Gera resposta com base nas faces e pets identificados na imagem
        response_body = generate_response_body_v2(bucket, imageName, faces, labels)

        # Loga a resposta no CloudWatch
        print(response_body)

        response = {
            "statusCode": 200,
            "body": json.dumps(response_body)
        }

        return response
    
    # Tratamento de erros
    except Exception as e:
        response = {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
        return response