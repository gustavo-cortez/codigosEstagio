import boto3

# Função para processar rostos
def process_faces(bucket, imageName):
    rekognition = boto3.client('rekognition')
    
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': imageName
            }
        },
        Attributes=['ALL']
    )
    return response['FaceDetails']

# Função para processar labels
def process_labels(bucket, imageName,):
    rekognition = boto3.client('rekognition')
    
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': imageName
            }
        },
        MaxLabels=10
    )
    return response['Labels']