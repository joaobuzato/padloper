from tkinter import *
import json
import os

# Diretório atual do script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Diretório raiz do projeto (subindo um nível)
ROOT_DIR = os.path.dirname(CURRENT_DIR)

# Caminho para o arquivo map.json na raiz do projeto
json_map = os.path.join(ROOT_DIR, 'map.json')

def save_settings(width_entry, height_entry, color_entry, settings_window):
    width = width_entry.get()
    height = height_entry.get()
    color = color_entry.get()
    
    # Read the existing JSON data
    with open(json_map, 'r') as file:
        data = json.load(file)
    
    # Update the JSON data with the new settings
    data['screen']['width'] = int(width)
    data['screen']['height'] = int(height)
    data['screen']['color'] = color
    
    # Save the updated JSON data back to map.json
    with open(json_map, 'w') as file:
        json.dump(data, file, indent=4)
    
    settings_window.destroy()

def open_settings_window():
    settings_window = Toplevel()
    settings_window.title("Settings")
    settings_window.config(padx=50, pady=50)

    with open(json_map, 'r') as file:
        data = json.load(file)
        screen_data = data.get('screen', {})
        width = screen_data.get('width', '')
        height = screen_data.get('height', '')
        color = screen_data.get('color', '')

    width_label = Label(settings_window, text="Width:")
    width_label.grid(row=0, column=0, padx=10, pady=10)
    width_entry = Entry(settings_window, width=30)
    width_entry.grid(row=0, column=1, padx=10, pady=10)
    width_entry.insert(0, width)

    height_label = Label(settings_window, text="Height:")
    height_label.grid(row=1, column=0, padx=10, pady=10)
    height_entry = Entry(settings_window, width=30)
    height_entry.grid(row=1, column=1, padx=10, pady=10)
    height_entry.insert(0, height)

    color_label = Label(settings_window, text="Color:")
    color_label.grid(row=2, column=0, padx=10, pady=10)
    color_entry = Entry(settings_window, width=30)
    color_entry.grid(row=2, column=1, padx=10, pady=10)
    color_entry.insert(0, color)

    save_button = Button(settings_window, text="Save", command=lambda: save_settings(width_entry, height_entry, color_entry, settings_window), width=16)
    save_button.grid(row=3, column=0, padx=10, pady=10)

    cancel_button = Button(settings_window, text="Cancel", command=settings_window.destroy, width=16)
    cancel_button.grid(row=3, column=1, padx=10, pady=10)