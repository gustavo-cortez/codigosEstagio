# Chatbot AcolhePet


## 📝 Resumo do projeto

O projeto consiste em um chatbot inovador que transforma o atendimento de ONGs dedicadas à doação de animais de estimação. Integrado ao Telegram, o chatbot automatiza processos essenciais, permitindo que as ONGs se concentrem em sua missão principal. Ele fornece imagens sobre animais disponíveis para adoção, agiliza a conexão com possíveis adotantes, e facilita o recrutamento de voluntários. Além disso, oferece dicas de cuidados com os pets, informações sobre eventos, e respostas rápidas a perguntas frequentes, melhorando a eficiência operacional e enriquecendo a experiência dos usuários.








***

## 💻 Funcionamento do sistema

### 🤖 Chatbot

O chatbot desenvolvido para o projeto tem como objetivo principal otimizar o atendimento das ONGs que realizam doações de PETs. Ele está integrado ao Telegram e oferece várias funcionalidades para facilitar a interação com os usuários:

#### Integração com o Telegram

 O chatbot opera diretamente no Telegram, permitindo uma comunicação ágil e acessível com os usuários. Isso torna mais fácil para os usuários se conectarem com as ONGs e obterem informações sobre adoção, doações, voluntariado, e outros serviços.

- **Serviços Oferecidos:**
    - **Adotar um Pet:** O chatbot fornece imagens dos animais disponíveis para adoção, permitindo que os usuários conheçam suas características antes de tomar uma decisão.
    - **Fazer uma Doação:** Os usuários podem contribuir com doações em dinheiro ou itens essenciais para a ONG, ajudando a manter os cuidados com os animais e as operações da organização.
    - **Voluntariar-se:** O bot oferece informações sobre como se voluntariar para ajudar em serviços na ONG, facilitando o engajamento de pessoas interessadas em apoiar a causa.
    - **Informações sobre a ONG:** Os usuários podem acessar dados e históricos da ONG, entendendo melhor suas missões, objetivos e impacto na comunidade.
    - **Serviços de Dicas:** O chatbot gera dicas personalizadas sobre cuidados com o pet e resgate de animais usando o Amazon Bedrock, com base na identificação de animais feita pelo Amazon Rekognition.

- **Identificação de Animais via Imagem:** Com o uso do Amazon Rekognition, os usuários podem enviar fotos de animais para o chatbot, que identifica o tipo de animal na imagem. Essa identificação é usada para gerar dicas apropriadas através do Amazon Bedrock.

- **Conversão de Texto em Áudio:** Para melhorar a acessibilidade, o chatbot utiliza o Amazon Polly para converter mensagens de texto em áudio. Os usuários têm a opção de ouvir as dicas e informações fornecidas pelo bot, tornando a interação mais inclusiva.

- **Armazenamento de Dados:** Fotos dos animais são armazenadas no Amazon S3, garantindo que o chatbot tenha acesso rápido a dados atualizados para fornecer aos usuários.


## 🏛️ Arquitetura do projeto
![Arquitetura inicial do projeto](assets/Diagrama.jpg)


## 🛠️ Tecnologias e Ferramentas

[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/Git-232F3E?logo=git&logoColor=red">](https://git-scm.com/)
[<img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=violet">](https://github.com/)

[<img src="https://img.shields.io/badge/AWS-fda100?logo=amazon-web-services&logoColor=white">](https://aws.amazon.com/pt/)
[<img src="https://img.shields.io/badge/AWS-CLI-fa8818?logo=amazon-web-services&logoColor=fda100&labelColor=232F3E">](https://aws.amazon.com/pt/cli/)
[<img src="https://img.shields.io/badge/AWS-S3-dd2304?logo=amazon-web-services&logoColor=fda100&labelColor=232F3E">](https://aws.amazon.com/pt/s3/)
[<img src="https://img.shields.io/badge/Amazon-DynamoDB-4053D6?logo=amazon-web-services&logoColor=fda100&labelColor=232F3E">](https://aws.amazon.com/pt/pm/dynamodb/)
[<img src="https://img.shields.io/badge/Amazon-Bedrock-01ac71?logo=amazon-web-services&logoColor=fda100&labelColor=232F3E">](https://aws.amazon.com/pt/bedrock/)
[<img src="https://img.shields.io/badge/Amazon-Rekognition-2a7abc?logo=amazon-web-services&logoColor=fda100&labelColor=232F3E">](https://aws.amazon.com/pt/rekognition/)
[<img src="https://img.shields.io/badge/Amazon_Polly-FF9900?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/polly/)
[<img src="https://img.shields.io/badge/Amazon_Lex-FF9900?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/lex/)
[<img src="https://img.shields.io/badge/Amazon_Lambda-FF9900?logo=amazon-aws&logoColor=white">](https://aws.amazon.com/lambda/)



[<img src="https://img.shields.io/badge/Serverless_Framework-ff5242?logo=serverless&logoColor=white">](https://www.serverless.com)

#### Plataforma integrada ao bot:
[<img src="https://img.shields.io/badge/Telegram-24A1DE?logo=Telegram&logoColor=white">](https://web.telegram.org/k/)


#### Ferramentas de comunicção do time:

[<img src="https://img.shields.io/badge/Discord-5865F2?logo=discord&logoColor=white">](https://discord.com/)
[<img src="https://img.shields.io/badge/Trello-0079BF?logo=trello&logoColor=white">](https://trello.com/)
[<img src="https://img.shields.io/badge/Whatsapp-25d366?logo=whatsapp&logoColor=white">](https://www.whatsapp.com/?lang=pt_BR)

***

## 📌 Como instalar a aplicação

### Clone o repositório

```bash
$ git clone https://github.com/Compass-pb-aws-2024-MARCO/sprints-9-10-pb-aws-marco.git 
```

### Acesse a pasta do projeto no terminal/cmd:

```bash
$ cd sprints-9-10-pb-aws-marco
```

### Realize um check-out para a branch de desenvolvimento:

```bash
$ git checkout grupo-04
```

### Cerfitique-se ue tem o serverless instalado:

```bash
$ serverless
$ npm install -g serverless
$ npm install serverless-python-requirements 
```

### Configure suas credenciais aws:
````bash
$ aws configure 
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE 
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY 
Default region name [None]: us-east-1 
Default output format [None]: ENTER 
````

### Acesse a pasta chatbotApi e execute o deploy:

```bash
$ cd chatbotApi
$ serverless deploy
```
> **Observação 1**: Siga o exemplo contido no arquivo .env.example e configure as variaveis de ambiente para rodar o projeto adequadamente. 

> **Observação 2:**: Quando for utilizar o Bedrock, solicite acesso ao amazon.titan-text-express-v1 atravéz do console da AWS.

---

## 👨‍💻 Autor
- [Gustavo Cortez](https://github.com/gustavo-cortez)



