# install requests
import requests
import json

# request -> response
# - URL, Verb (GET, POST, PUT, PATCH), Headers, Body, Params
# - Status code, Status text, Body, Headers

def save_pokemon(character):
  try:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{character.lower()}")
    response.raise_for_status() 

    data = response.json()

    with open(f"{character.lower()}.json", "w") as file:
      file.write(json.dumps(data, indent=2))
  except:
    print("Whoops! Something went wrong!")

save_pokemon("pikachu")