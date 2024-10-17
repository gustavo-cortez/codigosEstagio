// dogController.js
import { getRandomDogImage } from '../Services/dogServices.js';

document.getElementById('fetchButton').addEventListener('click', () => {
    renderDog();
});

document.getElementById('nameDog').addEventListener('change', () => {
    renderDog()
});

const renderDog = async () => {
    const breed = document.getElementById('nameDog').value.toLowerCase();
    
    getRandomDogImage(breed)
        .then(imageUrl => {
            const dogImageContainer = document.getElementById('dogImageContainer');
            dogImageContainer.innerHTML = `<img src="${imageUrl}" alt="Random Dog">`;
        })
        .catch(error => console.error('Erro:', error));
}
