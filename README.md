<div align=center>
  
  # API Pokédex

Esta API visa facilitar o consumo da API pública PokeAPI por meio de padronização de dados e endpoints preparados
</div>



## Funções disponíveis: 
  ### URL:
  http://localhost:8000/index/?offset=<deslocamento>&quantity=<quantidade de pokémons>
  
  ### Retorna dados dos próximos [x] pokémons com base no índice (recebe parâmetro de deslocamento)
  Útil para telas iniciais ou telas de listagem, que precisam solicitar quantidades consideráveis de pokémons rapidamente

  ### Dados:
  - "name": String (nome do pokémon)
  - "id": int (índice do pokemon/id único)
  - "thumb_image": String (url de imagem de thumbnail do pokémon)
  
<hr>


  ### URL:
  http://localhost:8000/pokemon/?id=<nome[string]/id do pokémon[int]>
  
  ### Envia requisição dos dados de um pokémon específico por nome ou índice na pokédex
  ### Dados:
  - "id": int (índice do pokemon/id único)
  - "name": String (nome do pokémon)
  - "image": String (url de arte oficial do pokémon)
  - "species_desc": String (descritivo do pokémon)
  - "types": List<String> (Lista de tipo(s) do pokémon)
  - "flavor-text": String (texto de ambientação)
  - "color": String (cor dominante, útil para customização no front-end)
