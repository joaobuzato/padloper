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

def screen():
    screen_window = Tk()
    screen_window.title("Screen")
    screen_window.config(padx=50, pady=50)

    hello = Button(text="Hello", command=print("hello"), width=16)
    hello.grid(row=1, column=1)
    screen_window.mainloop()

window.config(padx=50, pady=50)

screen_button = Button(text="Screen", command=screen, width=16)

screen_button.grid(row=1, column=1)

build_button = Button(text="Build", command=build, width=16)

build_button.grid(row=10, column=1)

run_button = Button(text="Run", command=run,  width=16)

run_button.grid(row=10, column=2)

window.mainloop()

