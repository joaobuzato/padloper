from tkinter import *
import os

window = Tk()
window.title("Padloper")

def build():
    os.system('python3 game_builder.py')
    pass

def run():
    os.system('python3 src/padmain.py')
    pass

window.config(padx=50, pady=50)
build_button = Button(text="Build", command=build, width=16)

build_button.grid(row=1, column=1)

run_button = Button(text="Run", command=run, width=16)

run_button.grid(row=2, column=1)

window.mainloop()