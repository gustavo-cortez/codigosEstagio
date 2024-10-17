// dogServices.js
export async function getRandomDogImage(breed) {
    const apiUrl = `https://dog.ceo/api/breed/${breed}/images/random`;
    try {
        const response = await axios.get(apiUrl);
        if (response.status !== 200) {
            throw new Error(`Erro ao buscar imagem: ${response.statusText}`);
        }
        return response.data.message;
    } catch (error) {
        console.error('Erro ao buscar imagem:', error.message);
        alert("Dog not found, try again");
        throw error;
    }
}
