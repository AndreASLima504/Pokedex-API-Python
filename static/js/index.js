var gOffset = 1;


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
    var pokemonsList = await request20pokemons(gOffset);
    const gridContainer = document.getElementById("pokemonGrid");
    var frag = document.createDocumentFragment();

    pokemonsList.forEach(p => {
    var pokeName = p["name"],
        pokeId = p["id"],
        pokeImg = p["thumbImage"];


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
    console.log(gOffset)
    gOffset += 20;
}

async function loopTest(){
    for (let index = 0; index < 4; index++) {
        await showMorePokemons(); // Espera cada chamada de showMorePokemons() completar antes de prosseguir
    }
}

loopTest()