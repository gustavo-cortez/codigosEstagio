// Adiciona um event listener para o evento de clique no botão com o id "button"
document.getElementById("button").addEventListener('click',()=>{
    // Obtém o valor do input com o id "inputName"
    let inputValue = document.getElementById('inputName').value 
    // Obtém o elemento com o id "details"
    let details = document.getElementById("details")
    // Limpa o conteúdo do elemento "details"
    details.innerHTML = ""
    // Realiza uma requisição fetch para a API do The Meal DB, buscando receitas com base no valor do input
    fetch(`https:www.themealdb.com/api/json/v1/1/search.php?s=${inputValue}`)
        .then(response => response.json())
        .then(data=> {
            // Obtém o elemento com o id "items"
            const items = document.getElementById("items")
            // Limpa o conteúdo do elemento "items"
            items.innerHTML = ""
            // Verifica se não há receitas encontradas
            if(data.meals == null){
                // Exibe uma mensagem informando que não foram encontradas receitas
                document.getElementById("msg").style.display = "block"
            }else{
                // Oculta a mensagem de erro
                document.getElementById("msg").style.display = "none"
                // Itera sobre as receitas encontradas
                data.meals.forEach(meal =>{
                    // Cria um novo elemento div para cada receita encontrada
                    itemDiv = document.createElement("div")
                    itemDiv.className = "m-2 singleItem"
                    // Define um evento de clique para exibir os detalhes da receita
                    itemDiv.setAttribute('onclick' , `details('${meal.idMeal}')`)
                    // Cria o HTML com as informações básicas da receita
                    let  itemInfo = `
                    <div class="card " style="width: 12rem;">
                        <img src="${meal.strMealThumb}" class="card-img-top" alt="...">
                        <div class="card-body text-center">
                            <h5 class="card-text">${meal.strMeal}</h5>
                        </div>
                    </div>
                    `
                    // Define o HTML dentro do elemento div criado
                    itemDiv.innerHTML = itemInfo
                    // Adiciona o elemento div à lista de itens
                    items.appendChild(itemDiv)
                })
            }

        })
})

// Função para obter os detalhes de uma receita específica
function details(id){
    // Realiza uma requisição fetch para a API do The Meal DB, buscando os detalhes da receita com base no id
    fetch(`https:www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then(res=>res.json())
    .then(detail => {
        // Obtém os detalhes da receita
        let meal = detail.meals[0]
        // Obtém o elemento com o id "details"
        let details = document.getElementById("details")
        // Limpa o conteúdo do elemento "details"
        details.innerHTML = ""
        // Cria um novo elemento div para exibir os detalhes da receita
        let detailsDiv = document.createElement("div")
        // Cria o HTML com os detalhes da receita
        let detailsInfo = `
        <div class="card " style="width: 40rem;">
            <img src="${meal.strMealThumb}" class="card-img-top" alt="...">
            <div class="card-body ">
                <h3 class="card-text">${meal.strMeal}</h3>
                <h6>Instrucitions</h6>
                <ul>
                    <li>${meal.strInstructions}</li>
                </ul>  
                <h6>Country and Category</h6>
                <ul>
                    <li>${meal.strArea}</li>
                    <li>${meal.strCategory}</li>
                </ul>  
                <h6>Ingredients</h6> 
                <ul> 
                    <li>${meal.strIngredient1}</li>
                    <li>${meal.strIngredient2}</li>
                    <li>${meal.strIngredient3}</li>
                    <li>${meal.strIngredient4}</li>
                    <li>${meal.strIngredient5}</li>
                </ul>
            </div>
        </div>
        `
        // Define o HTML dentro do elemento div criado
        detailsDiv.innerHTML = detailsInfo
        // Adiciona o elemento div à área de detalhes
        details.appendChild(detailsDiv)
    })
}
