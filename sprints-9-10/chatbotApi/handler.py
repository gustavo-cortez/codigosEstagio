# Importações das bibliotecas necessárias
import requests
from routes.telegramToLex import telegramToLex
from routes.textToSpeech import textToSpeech
from routes.generateTips import generateCareProcedures
from routes.analyzeImage import handleImage

# Definição das funções para o Serverless Framework
def telegramToLex_handler(event, context):
    return telegramToLex(event, context)

def textToSpeech_handler(event, context):
    return textToSpeech(event, context)

def textToSpeech_handler(event, context):
    return textToSpeech(event, context)

def generateTips_handler(event, context):
    return generateCareProcedures(event, context)

def analyzeImage_handler(event, context):
    return handleImage(event, context)
