from tkinter import *
import json
import os

# Diretório atual do script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Diretório raiz do projeto (subindo um nível)
ROOT_DIR = os.path.dirname(CURRENT_DIR)

# Caminho para o arquivo map.json na raiz do projeto
json_map = os.path.join(ROOT_DIR, 'map.json')

def save_scoreboard_settings(position_var, size_entry, font_entry, color_entry, settings_window):
    position = position_var.get()
    size = size_entry.get()
    font = font_entry.get()
    color = color_entry.get()
    
    # Read the existing JSON data
    with open(json_map, 'r') as file:
        data = json.load(file)
    
    # Update the JSON data with the new settings
    data['scoreboard']['position'] = position
    data['scoreboard']['size'] = int(size)
    data['scoreboard']['font'] = font
    data['scoreboard']['color'] = color
    
    # Save the updated JSON data back to map.json
    with open(json_map, 'w') as file:
        json.dump(data, file, indent=4)
    
    settings_window.destroy()

def open_scoreboard_window():
    settings_window = Toplevel()
    settings_window.title("Scoreboard Settings")
    settings_window.config(padx=50, pady=50)

    with open(json_map, 'r') as file:
        data = json.load(file)
        scoreboard_data = data.get('scoreboard', {})
        position = scoreboard_data.get('position', 'top')
        size = scoreboard_data.get('size', '')
        font = scoreboard_data.get('font', '')
        color = scoreboard_data.get('color', '')

    position_label = Label(settings_window, text="Position:")
    position_label.grid(row=0, column=0, padx=10, pady=10)
    position_var = StringVar(settings_window)
    position_var.set(position)
    position_dropdown = OptionMenu(settings_window, position_var, 'top', 'bottom')
    position_dropdown.grid(row=0, column=1, padx=10, pady=10)

    size_label = Label(settings_window, text="Size:")
    size_label.grid(row=1, column=0, padx=10, pady=10)
    size_entry = Entry(settings_window, width=30)
    size_entry.grid(row=1, column=1, padx=10, pady=10)
    size_entry.insert(0, size)

    font_label = Label(settings_window, text="Font:")
    font_label.grid(row=2, column=0, padx=10, pady=10)
    font_entry = Entry(settings_window, width=30)
    font_entry.grid(row=2, column=1, padx=10, pady=10)
    font_entry.insert(0, font)

    color_label = Label(settings_window, text="Color:")
    color_label.grid(row=3, column=0, padx=10, pady=10)
    color_entry = Entry(settings_window, width=30)
    color_entry.grid(row=3, column=1, padx=10, pady=10)
    color_entry.insert(0, color)

    save_button = Button(settings_window, text="Save", command=lambda: save_scoreboard_settings(position_var, size_entry, font_entry, color_entry, settings_window), width=16)
    save_button.grid(row=4, column=0, padx=10, pady=10)

    cancel_button = Button(settings_window, text="Cancel", command=settings_window.destroy, width=16)
    cancel_button.grid(row=4, column=1, padx=10, pady=10)