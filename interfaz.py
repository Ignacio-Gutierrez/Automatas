from main import AutomasYGramatica as ag
import csv
import re
import pandas as pd
from tkinter import Tk, Frame, Label, Entry, Button, filedialog

class Interfaz:
    def __init__(self):
        self.root = Tk()
        self.root.title('Autómatas y Gramática')
        self.root.geometry('1000x574')
 
        self.create_frames()
        self.create_widgets()

        self.root.mainloop()

    def create_frames(self):
        self.frame1 = Frame(self.root, width=1000, height=100)
        self.frame1.configure(bg='#77dd77')
        self.frame1.pack(side='top')

        self.frame2 = Frame(self.root, width=1000, height=428)
        self.frame2.pack(side='top')

        self.frame3 = Frame(self.root, width=1000, height=46)
        self.frame3.configure(bg='#77dd77')
        self.frame3.pack(side='top')

    def create_widgets(self):

        btn_imp = Button(self.frame1, text='Importar', command=lambda:ag().import_file(), font=30)
        btn_imp.place(x=20, y=20, width=125, height=30)

        btn_exp = Button(self.frame1, text='Exportar', font=30)
        btn_exp.place(x=855, y=20, width=125, height=30)

        btn_start = Button(self.frame1, text='Iniciar', command=lambda:ag().start(self.txt1.get(), self.txt2.get()), font=30)
        btn_start.place(x=650, y=17, width=65, height=65)

        btn_stop = Button(self.frame3, text='Salir', command=lambda:ag.close(self.root), font=30)
        btn_stop.place(x=855, y=8, width=125, height=30)


        lbl1 = Label(self.frame1, text='Fecha de inicio "AAAA-MM-DD":', font=12)
        lbl1.place(x=250, y=18, width=255, height=25)
        lbl1.configure(bg='#77dd77')
        self.txt1 = Entry(self.frame1, bg='white', fg='black')
        self.txt1.place(x=515, y=18, width=100, height=25)

        lbl2 = Label(self.frame1, text='Fecha de fin "AAAA-MM-DD":', font=12)
        lbl2.place(x=250, y=55, width=255, height=25)
        lbl2.configure(bg='#77dd77')
        self.txt2 = Entry(self.frame1, bg='white', fg='black')
        self.txt2.place(x=515, y=55, width=100, height=25)

        lbl3 = Label(self.frame3, text=f'Datos Importados: {ag().data_imp}', font=12)
        lbl3.configure(bg='#77dd77')
        lbl3.place(x=40, y=3, width=250, height=40)

        lbl4 = Label(self.frame3, text=f'Conectados: {ag().connected}', font=12)
        lbl4.configure(bg='#77dd77')
        lbl4.place(x=345, y=3, width=200, height=40)

        lbl5 = Label(self.frame3, text=f'Errores: {ag().errors}', font=12)
        lbl5.configure(bg='#77dd77')
        lbl5.place(x=600, y=3, width=170, height=40)

app = Interfaz()