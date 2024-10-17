import boto3

# Gera o áudio a partir do texto usando AWS Polly.
def synthesize_speech(text, voice_id='Camila'):
    polly_client = boto3.client('polly')
    try:
        response = polly_client.synthesize_speech(Text=text, OutputFormat='mp3', VoiceId=voice_id)
        return response['AudioStream'].read()
    except Exception as e:
        print(f"Error synthesizing speech: {e}")
        return None