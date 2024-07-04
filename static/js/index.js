var gOffset = 1;
var page = 0

async function request20pokemons(offset){
    var response = await fetch("http://127.0.0.1:5000/", {
        method: 'POST',
        body: JSON.stringify([offset]),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
          }
    })
    var json = await response.json();
    return json;
}

async function showMorePokemons() {
    const startTime = performance.now();
    var pokemonsList = await request20pokemons(page * 20 + 1);
    const gridContainer = document.getElementById("pokemonGrid");
    var frag = document.createDocumentFragment();

    pokemonsList.forEach(p => {
    var pokeName = p["name"],
        pokeId = p["id"],
        pokeImg = p["thumb_image"];


    var temp = document.createElement('div');
    temp.classList.add("pokemonThumb")
    temp.innerHTML =    `<div class="pokemonThumb">
                        <img src="${pokeImg}" alt="">
                        <div class="pokemonInfo">
                            <span class="pokemonName">${pokeName}</span>
                            <span class="pokemonId">#${pokeId}</span>
                        </div>
                    </div>`
    while(temp.firstChild){
        frag.appendChild(temp.firstChild);
    }
    });
    gridContainer.appendChild(frag)
    const endTime = performance.now()

    console.log("Tempo decorrido: " + (endTime - startTime))
}

