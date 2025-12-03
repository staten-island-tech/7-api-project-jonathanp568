import requests

def getChar(char):
    response = requests.get(f"https://rickandmortyapi.com/api/")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
    }

character = getChar("Jaguar")
print(character)