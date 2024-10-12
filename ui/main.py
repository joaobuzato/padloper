from tkinter import *
import os
import json
from settings_window import open_settings_window

# Diretório atual do script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Diretório raiz do projeto (subindo um nível)
ROOT_DIR = os.path.dirname(CURRENT_DIR)

# Caminho para o arquivo map.json na raiz do projeto
json_map = os.path.join(ROOT_DIR, 'map.json')

window = Tk()
window.title("Padloper")
ENV = "python3"
def build():
    name = game_name_entry.get()
    
    # Read the existing JSON data
    with open(json_map, 'r') as file:
        data = json.load(file)
    
    # Update the JSON data with the game name
    data['name'] = name
    
    # Save the updated JSON data back to map.json
    with open(json_map, 'w') as file:
        json.dump(data, file, indent=4)
    
    os.system(f'{ENV} ./game_builder.py')

def run():
    os.system(f'{ENV} ./src/padmain.py')

def screen():
    screen_window = Tk()
    screen_window.title("Screen")
    screen_window.config(padx=50, pady=50)

    hello = Button(text="Hello", command=print("hello"), width=16)
    hello.grid(row=1, column=1)
    screen_window.mainloop()

window.config(padx=50, pady=50)

with open(json_map, 'r') as file:
    data = json.load(file)
    game_name = data.get('name', '')

game_name_label = Label(window, text="Game Name:")
game_name_label.grid(row=0, column=0, padx=10, pady=10)
game_name_entry = Entry(window, width=30)
game_name_entry.grid(row=0, column=1, padx=10, pady=10)
game_name_entry.insert(0, game_name)

build_button = Button(text="Build", command=build, width=16)
build_button.grid(row=10, column=1)

run_button = Button(text="Run", command=run,  width=16)
run_button.grid(row=10, column=2)

settings_button = Button(window, text="Settings", command=open_settings_window, width=16)
settings_button.grid(row=10, column=3)

window.mainloop()

