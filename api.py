import requests
import tkinter as tk

def getChar(char):
    response = requests.get(f"https://rickandmortyapi.com/api/character")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    return {
        "name": data["results"][0]["name"],
        "status": data["results"][0]["status"],
        "species": data["results"][0]["species"],
        "origin": data["results"][0]["origin"]["name"]
        }
character = getChar("f")
print(character)