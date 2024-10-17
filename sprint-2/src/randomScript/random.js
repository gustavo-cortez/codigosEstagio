// random.js

async function getRandomMeal() {
    try {
        // Realiza uma requisição pelo axios para a API do The Meal DB gerando uma receita aleatória
        const response = await axios.get('https://www.themealdb.com/api/json/v1/1/random.php');
        const meal = response.data.meals[0];
        // Cria um novo elemento div para exibir os detalhes da receita aleatória
        const detailsDiv = document.getElementById('details');
        // Cria o HTML com os detalhes da receita aleatória
        detailsDiv.innerHTML = `
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
        `;
    } catch (error) {
        console.error('Error fetching random meal:', error);
    }
}