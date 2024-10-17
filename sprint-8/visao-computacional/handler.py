import json
from controllers.v1_controller import v1_vision_controller
from controllers.v2_controller import v2_vision_controller

def health(event, context): #retorna o status de sucesso da execução da função
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "VISION api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_description(event, context):
    body = {
        "message": "VISION api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

# Rota 4
def v1_vision(event, context): #detecta face na imagem e retorna emoções
    return v1_vision_controller(event, context)
    
def v2_vision(event, context): #detecta animais 
    return v2_vision_controller(event, context)