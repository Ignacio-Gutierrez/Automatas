from main import Funciones
import csv
import re
import pandas as pd
from tkinter import Tk, Frame, Label, Entry, Button, filedialog, IntVar
from openpyxl import Workbook


class Interfaz:
    def __init__(self):
        self.root = Tk()
        self.root.title('Autómatas y Gramática')
        self.root.geometry('1000x574')

        self.func = Funciones()

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

        btn_imp = Button(self.frame1, text='Importar', command=self.func.import_file, font=30)
        btn_imp.place(x=20, y=20, width=125, height=30)

        btn_exp = Button(self.frame1, text='Exportar', command=self.func.export_file,font=30)
        btn_exp.place(x=855, y=20, width=125, height=30)

        btn_start = Button(self.frame1, text='Iniciar', command=lambda: self.func.start(self.txt2.get(), self.txt3.get()), font=30)
        btn_start.place(x=650, y=17, width=65, height=65)

        btn_stop = Button(self.frame3, text='Salir', command=lambda: Funciones.close(self.root), font=30)
        btn_stop.place(x=855, y=8, width=125, height=30)

        lbl1 = Label(self.frame1, text='Usuario:', font=12)
        lbl1.place(x=250, y=11, width=255, height=25)
        lbl1.configure(bg='#77dd77')
        self.txt1 = Entry(self.frame1, bg='white', fg='black')
        self.txt1.place(x=515, y=11, width=100, height=25)

        lbl2 = Label(self.frame1, text='Fecha de inicio "AAAA-MM-DD":', font=12)
        lbl2.place(x=250, y=37, width=255, height=25)
        lbl2.configure(bg='#77dd77')
        self.txt2 = Entry(self.frame1, bg='white', fg='black')
        self.txt2.place(x=515, y=37, width=100, height=25)

        lbl3 = Label(self.frame1, text='Fecha de fin "AAAA-MM-DD":', font=12)
        lbl3.place(x=250, y=63, width=255, height=25)
        lbl3.configure(bg='#77dd77')
        self.txt3 = Entry(self.frame1, bg='white', fg='black')
        self.txt3.place(x=515, y=63, width=100, height=25)

        lbl4_t = Label(self.frame3, text='Datos Importados:', font=12)
        lbl4_t.configure(bg='#77dd77')
        lbl4_t.place(x=40, y=3, width=150, height=40)
        lbl4_v = Label(self.frame3, textvariable=self.func.data_imp, font=12, anchor='w')
        lbl4_v.configure(bg='#77dd77')
        lbl4_v.place(x=190, y=3, width=100, height=40)

        lbl5_t = Label(self.frame3, text='Conectados:', font=12)
        lbl5_t.configure(bg='#77dd77')
        lbl5_t.place(x=345, y=3, width=100, height=40)
        lbl5_v = Label(self.frame3, textvariable=self.func.connected, font=12, anchor='w')
        lbl5_v.configure(bg='#77dd77')
        lbl5_v.place(x=445, y=3, width=100, height=40)

        lbl6_t = Label(self.frame3, text='Errores:', font=12)
        lbl6_t.configure(bg='#77dd77')
        lbl6_t.place(x=600, y=3, width=70, height=40)
        lbl6_v = Label(self.frame3, textvariable=self.func.errors, font=12, anchor='w')
        lbl6_v.configure(bg='#77dd77')
        lbl6_v.place(x=670, y=3, width=100, height=40)

app = Interfaz()