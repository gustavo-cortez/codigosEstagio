import hashlib
import boto3
import uuid
from boto3.dynamodb.conditions import Key

# Gera um hash SHA-256 a partir de uma frase
def generate_hash(phrase):
    return hashlib.sha256(phrase.encode()).hexdigest()

# Verifica se uma tabela DynamoDB existe
def check_table_exists(table_name):
    try:
        dynamo = boto3.client('dynamodb')
        existing_tables = dynamo.list_tables()['TableNames']
        return table_name in existing_tables
    except Exception as e:
        print(f"Error checking if table exists: {e}")
        return False

# Cria uma tabela DynamoDB se ela não existir
def create_table_if_not_exists(table_name):
    if not check_table_exists(table_name):
        try:
            dynamo = boto3.resource('dynamodb')
            table = dynamo.create_table(
                TableName=table_name,
                KeySchema=[{'AttributeName': 'unique_id', 'KeyType': 'HASH'}],
                AttributeDefinitions=[{'AttributeName': 'unique_id', 'AttributeType': 'S'}],
                BillingMode='PAY_PER_REQUEST'
            )
            table.wait_until_exists()
        except Exception as e:
            print(f"Error creating table: {e}")

# Verifica se uma frase, identificada por um unique_id, já existe em uma tabela DynamoDB
def check_text_in_dynamo(unique_id, table_name):
    try:
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table(table_name)
        response = table.get_item(Key={'unique_id': unique_id})
        return response.get('Item')
    except Exception as e:
        print(f"Error checking phrase in DynamoDB: {e}")
        return None

# Salva um item na tabela DynamoDB
def save_to_dynamo(item, table_name):
    try:
        dynamo = boto3.resource('dynamodb')
        table = dynamo.Table(table_name)
        table.put_item(Item=item)
    except Exception as e:
        print(f"Error saving item to DynamoDB: {e}")
