# Detecção de Rostos Com Classificação de Emoções e Detecção de Pet e Dicas Para o Pet
  
Este projeto implementa funcionalidades como  detectar rostos e identificar animais usando AWS Rekognition e AWS bedrock para gerar dicas personalizadas via de API usando AWS Lambda e API Gateway para processar imagens.
  
  
*** 
## Autor
- [Gustavo Cortez](https://github.com/gustavo-cortez)

***

## Um pouco sobre as rotas:

### GET
- Rota /: Nessa primeira rota é retornada a mensagem "Go Serverless v3.0! Your function executed successfully!".

- Rota /v1: Nessa segunda rota é retornada a mensagem "VISION api version 1.".

- Rota /v2: Nessa terceira rota é retornada a mensagem "VISION api version 2.".

### POST

#### Para as utilizar as rotas POST  é necessário acesso ter um bucket S3 na aws, onde deverá deixar armazenadas as imagens que deseja realizar as detecções.

#### O json enviado em ambas as rotas deve ter o seguinte formato:
```
{ 
   "bucket": "nomedobucket", 
   "imageName": "imagem.jpg" 
} 
```

- Rota /v1/vision: Nessa primeira rota POST, implementamos a detecção de faces e a classificação de emoções usando o serviço AWS Rekognition. Quando uma imagem é enviada para essa rota, o sistema identifica rostos e analisa as expressões faciais, fornecendo qual a emoção e nível de confiança que foi classificada a emoção. 

- Rota /v2/vision: Nessa segunda rota POST, o sistema identifica não apenas rostos, mas também animais de estimação (pets). Além disso, com base nas características dos animais detectados, são geradas dicas personalizadas para cuidados com os pets, com o AWS Bedrock. Por exemplo, se um gato é identificado na imagem, o sistema pode sugerir dicas relacionadas à alimentação, higiene ou brincadeiras para gatos.

***
## Arquitetura projeto:
  
![arquitetura-base](./assets/arquitetura-base.jpg)  

***

## 📂 Estrutura do projeto

```
└── 📁sprints-8-pb-aws-marco
    └── .gitignore
    └── README
    └── 📁assets
        └── arquitetura-base 
    └── 📁visao-computacional
        └── 📁controllers
            └── v1_controller
            └── v2_controller
        └── 📁services
            └── bedrock_service
            └── rekognition_service
            └── v1_response_service
            └── v2_response_service
        └── 📁utils
            └── face_utils
            └── generate_tips
            └── image_utils
        └── handler
        └── gitignore
        └── serverless   

```
---
## Tecnologias utilizadas no projeto

[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/Git-232F3E?logo=git&logoColor=red">](https://git-scm.com/)
[<img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=violet">](https://github.com/)
[<img src="https://img.shields.io/badge/AWS-fda100?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/pt/)
[<img src="https://img.shields.io/badge/AWS-CLI-232F3E?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/pt/cli/)
[<img src="https://img.shields.io/badge/AWS-S3-dd2304?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/pt/s3/)
[<img src="https://img.shields.io/badge/AWS-Cloudwatch-green?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/pt/cloudwatch/)
[<img src="https://img.shields.io/badge/Amazon-Bedrock-01ac71?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/pt/bedrock/)
[<img src="https://img.shields.io/badge/Amazon-Rekognition-blue?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/pt/rekognition/)
[<img src="https://img.shields.io/badge/Serverless_Framework-ff5242?logo=amazon-aws&logoColor=white">](https://www.serverless.com)


## Tecnologias utilizadas no comunicação do time:

[<img src="https://img.shields.io/badge/Trello-0079BF?logo=trello&logoColor=white">](https://trello.com/)
[<img src="https://img.shields.io/badge/Teams-6264A7?logo=microsoft-teams&logoColor=white">](https://www.microsoft.com/pt-br/microsoft-teams/group-chat-software)

***
## Acesso ao projeto 

### Clone o repositório

```bash
$ git clone https://github.com/Compass-pb-aws-2024-MARCO/sprint-8-pb-aws-marco.git
```
### Faça acesso da pasta da Sprint 8 

```bash
$ cd sprints-8-pb-aws-marco
```

### Faça o checkout para a branch 1

```bash
$ git checkout grupo-1
```

### Faça a instalação do framework Serverless

```bash
$ npm install -g serverless
```

### Insira as credenciais AWS

```
$ aws configure
AWS Access Key ID: ACCESSKEYEXAMPLE
AWS Secret Access Key: SECRETKEYEXAMPLE
Default region name [None]: us-east-1
Default output format [None]: ENTER
```

### Efetue o Deploy  acessando a pasta visão-computacional

```bash
$ serverless deploy
```
*** 
  
## Formato dos links gerados
  #### GET - https://xxxxxxxxx.execute-api.us-east-1.amazonaws.com/

  #### GET - https://xxxxxxxxx.execute-api.us-east-1.amazonaws.com/v1

  #### GET - https://xxxxxxxxx.execute-api.us-east-1.amazonaws.com/v2

  #### POST - https://xxxxxxxxx.execute-api.us-east-1.amazonaws.com/v1/vision

  #### POST - https://xxxxxxxxx.execute-api.us-east-1.amazonaws.com/v2/vision

## Exemplo de teste v2 - Entrada de dados
```
{ 
   "bucket": "photossprint8", 
   "imageName": "iStock-1271494334-750x325.jpg" 
} 
```

## Exemplo de teste v2 - Saída de dados
```bash
{
  "url_to_image": "https://photossprint8.s3.amazonaws.com/iStock-1271494334-750x325.jpg",
  "created_image": "01-07-2024 12:13:51",
  "pets": [
    {
      "labels": [
        {
          "Confidence": 96.1084594726563,
          "Name": "Animal"
        },
        {
          "Confidence": 96.1084594726563,
          "Name": "Dog"
        },
        {
          "Confidence": 96.1084594726563,
          "Name": "Pet"
        },
        {
          "Confidence": 96.1084594726563,
          "Name": "Golden Retriever"
        }
      ],
      "Dicas": "Dicas sobre Golden Retriever: Nível de Energia e Necessidades de Exercícios:O Golden Retriever é uma raça de cão que tem um nível de energia alto. É recomendado que os cães de este tipo sejam exercitados regularmente, como caminhadas, jogs e atividades de play. Ao mesmo tempo, é importante garantir que os cães tenham acesso a um espaço adequado para que possam exercer suas energias de maneira saudável.Temperamento e Comportamento:O Golden Retriever é um cão cariñoso, amigável e inteligente. É um cão que gosta de estar em companhia de seus humanos e é excelente para casas com crianças. Eles são facilmente trainados e podem aprender comandos e tricks.Cuidados e Necessidades:O Golden Retriever precisa de cuidados específicos para mantê-lo saudável e feliz. É importante darle alimento de qualidade, que contemple os nutrientes necessários para os cães de raça grande. Também é necessário regularmente lavar o pelo do cão para evitar que se pegue mal ou tenha um odor desagradável.Problemas de Saúde Comuns:Alguns dos problemas de saúde comuns que podem ocorrer em cães Golden Retriever são hipoartrite, luxação de garganta e entropia da retina. É importante realizar exames regulares com o veterinário para detectar e tratar esses problemas oportunamente.(“Golden Retriever”, {URL})"
    },
    {
      "labels": [
        {
          "Confidence": 92.3313522338867,
          "Name": "Animal"
        },
        {
          "Confidence": 92.3313522338867,
          "Name": "Cat"
        },
        {
          "Confidence": 96.1084594726563,
          "Name": "Pet"
        },
        {
          "Confidence": 55.3336372375488,
          "Name": "Manx"
        }
      ],
      "Dicas": "Dicas sobre Manx: Nível de Energia e Necessidades de Exercícios:O Manx tem um nível de energia moderado e gosta de fazer exercícios leves. Ele é adequado para residências em apartamentos ou casas com pequenos espaços.Temperamento e Comportamento:O Manx é carinhoso, inteligente e alegre. Ele é sociável e gosta de interagir com os humanos. Ele pode ser independente, mas também é capaz de se adaptar bem a vida em casa.Cuidados e Necessidades:O Manx precisa de cuidados específicos para mantê-lo saudável. Ele deve ser alimentado com alimentos de qualidade, como ração especial para gatos de raça pequena, que são ricos em proteínas e baixos em carboidratos. Ele também precisa de higiene regular, como lavagem de pelo regular e cuidado dental.Problemas de Saúde Comuns:A menos que o Manx tenha alguma condição genética ou de saúde específica, ele não é particularmente propensa a problemas de saúde comuns. No entanto, como todos os gatos, ele pode ser afetado por infecções, gatilhos e outras doenças. É importante mantê-lo vacinado e consultar o veterinário regularmente para detectar e tratar problemas de saúde precoces.(\"Manx\", {URL})"
    }
  ]
}
```

