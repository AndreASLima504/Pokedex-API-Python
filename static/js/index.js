var offset = 1;

function request20pokemons(){

}

function showMorePokemons() {
    var pokeName,
        pokeId,
        pokeImg;

    const gridContainer = document.getElementById("pokemonGrid");

    var frag = document.createDocumentFragment(),
        temp = document.createElement('div');
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
    gridContainer.appendChild(frag)
    offset += 20;
}



