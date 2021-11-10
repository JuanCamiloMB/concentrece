import subprocess
import tkinter
import os


def exec_facil():
    actual_path = os.getcwd()

    subprocess.call(['C:/Users/juanc/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Python 3.9',
                     actual_path + '/lvl_facil/lvl_facil.py'])


ventana = tkinter.Tk()
ventana.title('Concentrece')
ventana.geometry('400x400')
ventana.configure(background='white')

titulo = tkinter.Label(ventana, text='Bienvenido a concentrece', fg='black')
titulo.pack(fill=tkinter.X)

btn_lvl_facil = tkinter.Button(text='Facil', command=exec_facil)
btn_lvl_facil.pack(padx=20, pady=20, side=tkinter.LEFT)

btn_lvl_medio = tkinter.Button(text='Medio')
btn_lvl_medio.pack(padx=20, pady=20, side=tkinter.LEFT)

ventana.mainloop()





