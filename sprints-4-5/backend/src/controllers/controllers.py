from services.services import predict, registrar_log, tratar_dados
from flask import request, jsonify
from models.models import HotelReservation 

def inferencia():
    dados = HotelReservation(**request.json)
    dados_tratados = tratar_dados(dados.dict())  # Trata os dados antes da entrada
    predicao = predict(dados_tratados)  # Faz a inferência no modelo
    registrar_log(predicao, dados.dict())  # Registra o log no DynamoDB
    return jsonify({'predicao': predicao})
