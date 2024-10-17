const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();
const port = 2500;

// Middleware para servir arquivos como módulos
app.use((req, res, next) => {
  const filePath = path.join(__dirname, req.url);
  if (filePath.endsWith('.js')) {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        next();
        return;
      }
      res.type('module');
      res.send(data);
    });
  } else {
    next();
  }
});

// Configuração para servir arquivos estáticos da pasta 'public'
app.use(express.static('src'));

app.listen(port, () => {
  console.log(`Servidor rodando em http://localhost:${port}`);
});
