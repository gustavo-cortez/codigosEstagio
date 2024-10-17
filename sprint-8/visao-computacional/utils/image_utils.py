# Função para formatar url da imagem
def format_image_url(bucket, imageName):
    return f"https://{bucket}.s3.amazonaws.com/{imageName}"