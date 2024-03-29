from tkinter import *
import os

window = Tk()
window.title("Padloper")
ENV = "python3"
def build():
    os.system(f'python3 ./game_builder.py')

def run():
    os.system(f'python3 ./src/padmain.py')

def screen():
    screen_window = Tk()
    screen_window.title("Screen")
    screen_window.config(padx=50, pady=50)

    hello = Button(text="Hello", command=print("hello"), width=16)
    hello.grid(row=1, column=1)
    screen_window.mainloop()

window.config(padx=50, pady=50)

build_button = Button(text="Build", command=build, width=16)

build_button.grid(row=10, column=1)

run_button = Button(text="Run", command=run,  width=16)

run_button.grid(row=10, column=2)

window.mainloop()

