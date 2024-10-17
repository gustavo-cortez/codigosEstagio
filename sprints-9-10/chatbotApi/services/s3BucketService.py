import os
import boto3
import random
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()
s3 = boto3.client('s3')
# Faz o upload de um arquivo para um bucket do S3 e retorna a URL do arquivo
def upload_to_s3(file_path, bucket_name, s3_key):
    try:
        s3.upload_file(file_path, bucket_name, s3_key)
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{s3_key}"
        return s3_url
    except Exception as e:
        print(f"Erro ao tentar fazer upload para o S3: {e}")
        return None

S3_BUCKET = os.getenv('S3_BUCKET')
IMAGES_PER_REQUEST = 4

def get_animal_images(species):
    prefix = f'{species}/'
    response = s3.list_objects_v2(Bucket=S3_BUCKET, Prefix=prefix)
    images = [item['Key'] for item in response.get('Contents', []) if item['Key'].endswith(('jpg', 'jpeg', 'png'))]
    selected_images = random.sample(images, min(IMAGES_PER_REQUEST, len(images)))
    return [f'https://{S3_BUCKET}.s3.amazonaws.com/{image}' for image in selected_images]