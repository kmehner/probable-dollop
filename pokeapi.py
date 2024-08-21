import requests 
import json

# JSON responses take the form of a dictionary 

response = {
  "name": "Pikachu",
  "type": "electric",
  "base_experience": 112 
}

print(response["base_experience"])

response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu") # Request information from our API 

json_data = response.text
# print(json_data)

poke_data = response.json() 
# print(poke_data)

print(poke_data["name"].title()) # pokemon name 
print(poke_data["sprites"]["other"]["dream_world"]["front_default"]) # pokemon image 
print(poke_data["types"][0]["type"]["name"]) # pokemon type 
print(poke_data["id"]) #pokemon 

first_held_item = poke_data["held_items"][0]["item"]["name"]
print(first_held_item)

def pokedex():
  pokemon = input("Which pokemon are you looking for?")
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}")

  if response.status_code == 200:
    poke_data = response.json() 

    poke_dict = {
      "name": poke_data["name"],
      "sprite": poke_data["sprites"]["other"]["dream_world"]["front_default"], 
      "type": poke_data["types"][0]["type"]["name"], 
      "id": poke_data["id"]
    }

    # return poke_dict
    print(poke_dict)
  else:
    # return "Bad response, try again!"
    print("Bad response")
  

pokemon_data_from_api = pokedex()
# print(pokemon_data_from_api)