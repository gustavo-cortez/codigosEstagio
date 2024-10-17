import boto3
import pickle
import uuid
import datetime
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.preprocessing import StandardScaler
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


aws_access_key_id = ''
aws_secret_access_key = ''
aws_session_token = ''  

session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    aws_session_token=aws_session_token,
)

def verificar_credenciais():
    try:
        session.client('sts').get_caller_identity()
    except (NoCredentialsError, PartialCredentialsError):
        return False
    return True

def verificar_acesso_bucket(bucket_name):
    s3 = session.client('s3')
    try:
        s3.head_bucket(Bucket=bucket_name)
    except Exception as e:
        print(e)
        return False
    return True

# Verifica as credenciais da AWS
if not verificar_credenciais():
    print("Credenciais da AWS não estão configuradas corretamente.")
    exit()

# Verifica o acesso ao bucket
bucket_name = 'sagemakermodel'
if not verificar_acesso_bucket(bucket_name):
    print(f"Não foi possível acessar o bucket '{bucket_name}'.")
    exit()

# Baixa o modelo do S3
s3 = session.client('s3')
s3.download_file(bucket_name, 'hotel_reservations_model.pkl', 'hotel_reservations_model.pkl')

# Carrega o modelo
with open('hotel_reservations_model.pkl', 'rb') as file:
    modelo = pickle.load(file)

# Configura o cliente do DynamoDB
dynamodb = session.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('logs')



def predict(dados):
    # Faz a previsão
    predicao = modelo.predict(dados)
    
    return predicao.tolist()

def registrar_log(predicao, dados):
    log_item = {
        'id': str(uuid.uuid4()),  # Gera um ID único para cada log
        'timestamp': str(datetime.datetime.now()),  # Registra o horário atual
        'predicao': str(predicao),
        'dados': str(dados),
    }
    table.put_item(Item=log_item)

def tratar_dados(dados):
    # Converte os dados para um DataFrame do pandas
    df = pd.DataFrame(dados, index=[0])
    # Limpeza de dados
    # Por exemplo, preencher quaisquer valores NaN com 0
    df.fillna(0, inplace=True)

    # Verifica se todas as colunas são numéricas
    for col in df.columns:
        # Se a coluna não for numérica, tenta convertê-la
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Preenche quaisquer NaN que possam ter sido introduzidos pela conversão
    df.fillna(0, inplace=True)

    # StandardScaler para normalizar os dados
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)

    return df_scaled

