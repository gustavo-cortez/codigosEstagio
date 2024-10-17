const express = require('express');
const path = require('path');

const site = express();

const port = 3000;

site.use(express.static(path.join(__dirname + '')));

site.use(function(req, res) {
    res.status(400);
    return res.send(`404 Error: Resource not found`);
  });
  

site.listen(port, () => {
  console.log(`Servidor rodando na porta ${port}`);
});
