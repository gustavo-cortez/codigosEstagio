# Projeto: RecipesOnline - Site feito com o uso da API TheMealDB

O site é dedicado aos amantes da culinária que desejam ter acesso a receitas na palma de suas mãos, de forma rápida e fácil. Utilizando o banco de dados da API TheMealDB, disponibilizamos mais de 100 receitas para nossos usuários explorarem e desfrutarem da forma que preferirem.

***
Desenvolvido por: [Gustavo Cortez de Paula](https://github.com/gustavo-cortez).

***

## Tecnologias usadas
- HTML
- CSS
- JavaScript/Node.js
### Dependências do Node.js
- Axios
- Express.js

***

## Execução (Código Fonte)

Foram feitas duas funcionalidades, utilizando a API [themealdb API](https://themealdb.com/api.php), sendo elas a funcionalidade de gerar uma receita aleatória, fazendo uma requisição para a API utilizando [AXIOS](https://www.npmjs.com/package/axios) para mostrar uma receita aleatória, e a funcionalidade de procurar por receitas dinamicamente fazendo requisições a API, utilizando fetch.


***

## Organização do código fonte

Dentro da pasta src existem as pastas randomScript, contendo o arquivo random.js onde está a estrutura lógica para a funcionalidade de geração de uma receita aleatória consumida pela API. E também a pasta searchScript com o arquivo search.js onde se encontra a estrutura lógica para a funcionalidade de pesquisar uma comida pela API.<br>
Na raíz do projeto, se encontra o arquivo server.js, responsável pela criação do servidor e das rotas, usando [nodeJS](https://nodejs.org/en) e [express](https://expressjs.com/pt-br/).<br>
Ainda na raíz do projeto se encontra a pasta css com o arquivo style.css onde foi feita a estilização das páginas estáticas do projeto.<br>
Também na raíz do projeto, encontram-se as páginas estáticas index.html e random.html que apresentam visualmente as funcionalidades de pesquisa de uma receita e geração de uma receita aleatória, respectivamente.

***

## Como usar a aplicação

Para usar a aplicação, na página inicial, basta digitar o nome de um prato na barra  de pesquisa e clicar em search:![barra de pesquisa](image/image-1.png)
Ou, caso queira gerar uma receita aleatória, no canto superior esquerdo, pode trocar para a página de receita aleatória, selecionando random meal, aqui: ![alt text](image/image.png)<br>
caso queira trocar de receita aleatória, clique no botão randomize, que a aplicação irá gerar outra receita aleatóriamente.

**Especificações**:


Foram feitas duas funcionalidades, utilizando a API [themealdb API](https://themealdb.com/api.php), sendo elas a funcionalidade de gerar uma receita aleatória, puxada da api por [AXIOS](https://www.npmjs.com/package/axios), e a funcionalidade de procurar por receitas de determinado nome, utilizando fetch.
Passo a passo para iniciar o projeto:

- Fazer o clone do repositório via git rodando um $git clone git@github.com:Compass-pb-aws-2024-MARCO/sprint-2-pb-aws-marco.git;
- Entrar na branch da equipe, rodando: $git checkout equipe-4;
- Rodar no terminal de sua IDE de preferência: npm install para instalar as dependências;
- Rodar novamente no terminal: node server.js;
- Acessar em seu navegador o localhost:3000;
- Finalizado, pode usar a aplicação!

***







