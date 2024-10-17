FROM node:lts-alpine3.19

RUN mkdir -p /src/appDocker
WORKDIR /src/Server/appdocker
COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE 2500
CMD ["npm", "start"]