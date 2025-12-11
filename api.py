import requests
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

root = tk.Tk()
root.geometry("600x700")
root.title("Rick and Morty Index")
label = tk.Label(root, text="Rick and Morty Index", font=("Helvetica", 20))
label.pack(pady=20)
label = tk.Label(root, text="Type in an id)", font=("Helvetica", 14))
label.pack(pady=20)
entry_box = tk.Entry(root, width=30)
entry_box.pack(pady=20)
result_label = tk.Label(root, text="")
result_label.pack(pady=25)
image_label = tk.Label(root)
image_label.pack()
def change_image(url):
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    tk_img = ImageTk.PhotoImage(img)
    image_label.config(image=tk_img)
    image_label.image = tk_img
def getChar(char, chars):
    char = int(char)
    chars = int(chars)
    if chars > 20:
        chars = ((chars - 1) % 20) + 1
    char = (char - 1) // 20 + 1
    response = requests.get(f"https://rickandmortyapi.com/api/character?page={char}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    data = response.json()
    name = "name", data["results"][chars]["name"],
    status = "status", data["results"][chars]["status"],
    species = "species", data["results"][chars]["species"],
    origin = "origin", data["results"][chars]["origin"]["name"]
    images = data["results"][chars]["image"]
    result_label.config(text = f"{name}, {status}, {species}, {origin}")
    change_image(images)
def getinput():
    user_text = entry_box.get()
    getChar(user_text, user_text)
button = tk.Button(root, text="Submit", command=getinput)
button.pack()
button.place(x=275, y=200)
root.mainloop()
