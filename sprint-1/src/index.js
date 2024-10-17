//<!-- Autor: Gustavo Cortez de Paula -->//
//<!-- Avaliação Sprint 1 - Compass UOL / AWS -->//
//<!-- Sistema em JavaScript/HTML para verificação de PIN -->//
let pinAleatorio
let numerosUsados = []
let tentativas = 0

function reiniciar() {
    window.location.reload()
}


function carregar() {
   pinAleatorio = Math.floor(Math.random() * 998999) + 1000 //Número randômico de no mínimo de 4 dígitos e máximo de 6 dígitos
   console.log("PIN:" + pinAleatorio)
}

function compararNumeros() {
   const numero = Number(document.getElementById('inputBox').value)
   if (numero >= 1000 && numero < 1000000) {
        numerosUsados.push(' ' + numero)
        document.getElementById('tentativaAnterior').innerHTML = numerosUsados
        if (numero > pinAleatorio && Math.abs(numero - pinAleatorio) > 10000){//Se a diferença entre os número for maior que 1000 é considerado como muito/menor
            tentativas++
            document.getElementById('textOutput').innerHTML = 'O número PIN desejado é muito menor que o informado'
            document.getElementById('inputBox').value = ''
            document.getElementById('tentativas').innerHTML = tentativas
        }
        else if (numero > pinAleatorio && Math.abs(numero - pinAleatorio) < 10000){
            tentativas++
            document.getElementById('textOutput').innerHTML = 'O número PIN desejado é menor que o informado'
            document.getElementById('inputBox').value = ''
            document.getElementById('tentativas').innerHTML = tentativas
        }
        else if (numero < pinAleatorio && Math.abs(numero - pinAleatorio) > 10000){//Se a diferença entre os número for maior que 1000 é considerado como muito/menor
            tentativas++
            document.getElementById('textOutput').innerHTML = 'O número PIN desejado é muito maior que o informado'
            document.getElementById('inputBox').value = ''
            document.getElementById('tentativas').innerHTML = tentativas
        }
        else if (numero < pinAleatorio && Math.abs(numero - pinAleatorio) < 10000){
            tentativas++
            document.getElementById('textOutput').innerHTML = 'O número PIN desejado é maior que o informado'
            document.getElementById('inputBox').value = ''
            document.getElementById('tentativas').innerHTML = tentativas
        }
        else {
            tentativas++
            document.getElementById('textOutput').innerHTML = 'Parabéns!!! O número PIN informado está correto após ' + tentativas + ' tentativa(s).'
            document.getElementById('tentativas').innerHTML = tentativas
            document.getElementById('inputBox').setAttribute('Readonly', 'Readonly')
        }
   }
   else{
        document.getElementById('textOutput').innerHTML = 'O número PIN tem de ser de 4 dígitos ou máximo de 6 dígitos.'
        document.getElementById('inputBox').value = ''
   }
   
}