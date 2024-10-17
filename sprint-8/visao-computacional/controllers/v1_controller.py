import json
from services.rekognition_service import process_faces
from services.v1_response_service import generate_response_body_v1

# Função para lidar com a rota de reconhecimento de faces
def v1_vision_controller(event, context):
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

        # Processa a imagem usando o serviço de Rekognition
        faces = process_faces(bucket, imageName)
    
        # Gera resposta com base nas faces e identificadas na imagem
        response_body = generate_response_body_v1(bucket, imageName, faces)
        
        # Loga a resposta no CloudWatch
        print(response_body)
        
        response = {
            "statusCode": 200,
            "body": json.dumps(response_body)
        }

        return response

    # Tratamento de erros
    except ValueError as e:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": str(e)})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Internal server error"})
        }