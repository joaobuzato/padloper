from tkinter import *
import os

window = Tk()
window.title("Padloper")
ENV = "python"
def build():
    try: 
        if os.system(f'python3 ./game_builder.py') == 1:
            print("construído com sucesso.")
            ENV = "python"
            os.system(f'{ENV} ./game_builder.py')
        else: 
            ENV = "python3"
    except: 
        print("Erro ao construir o jogo")
    pass

def run():
    try:
        os.system(f'{ENV} ./src/padmain.py')
        
    except:
        os.system(f'python ./src/padmain.py')
    pass

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

