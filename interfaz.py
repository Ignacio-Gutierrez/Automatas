from main import Funciones
import csv
import re
import pandas as pd
from tkinter import Tk, Frame, Label, Entry, Button, filedialog, IntVar, ttk

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

        self.frame2 = Frame(self.root, width=1000, height=46)
        self.frame2.configure(bg='#91e38e')
        self.frame2.pack(side='top')

        self.frame3 = Frame(self.root, width=100, height=428)
        self.frame3.pack(side='top')

    def create_widgets(self):

        btn_imp = Button(self.frame1, text='Importar', command=self.tree_import, font=30)
        btn_imp.place(x=20, y=20, width=125, height=30)

        btn_exp_r = Button(self.frame1, text='Exportar', command=self.func.export_file_range,font=30, activebackground="#5785ff") #Lo buscado
        btn_exp_r.place(x=855, y=20, width=125, height=30)

        btn_exp_e = Button(self.frame1, text='Exportar Errores', command=self.func.export_file_error,font=("Arial", 11), activebackground="#ff5757") #Errores
        btn_exp_e.place(x=855, y=60, width=125, height=30)

        btn_start = Button(self.frame1, text='Iniciar', command=lambda: self.func.start(self.txt1.get(), self.txt2.get(), self.txt3.get()), font=30, activebackground="#5785ff")
        btn_start.place(x=650, y=17, width=65, height=65)
        btn_stop = Button(self.frame2, text='Salir', command=lambda:self.root.destroy(), bg="#ff7777",font=30, activebackground="#ff4c4c")
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

        lbl4_t = Label(self.frame2, text='Datos Importados:', font=12)
        lbl4_t.configure(bg='#91e38e')
        lbl4_t.place(x=40, y=3, width=150, height=40)
        lbl4_v = Label(self.frame2, textvariable=self.func.data_imp, font=12, anchor='w')
        lbl4_v.configure(bg='#91e38e')
        lbl4_v.place(x=190, y=3, width=100, height=40)

        lbl5_t = Label(self.frame2, text='Conexiones:', font=12)
        lbl5_t.configure(bg='#91e38e')
        lbl5_t.place(x=345, y=3, width=100, height=40)
        lbl5_v = Label(self.frame2, textvariable=self.func.connected, font=12, anchor='w')
        lbl5_v.configure(bg='#91e38e')
        lbl5_v.place(x=445, y=3, width=100, height=40)

        lbl6_t = Label(self.frame2, text='Errores:', font=12)
        lbl6_t.configure(bg='#91e38e')
        lbl6_t.place(x=600, y=3, width=70, height=40)
        lbl6_v = Label(self.frame2, textvariable=self.func.errors, font=12, anchor='w')
        lbl6_v.configure(bg='#91e38e')
        lbl6_v.place(x=670, y=3, width=100, height=40)

    def tree_import(self):

        if hasattr(self, "tree_table"):
            self.tree_table.destroy()
        
        if hasattr(self, "scrollbar"):
            self.scrollbar.destroy()

        self.func.import_file()
        
        self.tree_table = ttk.Treeview(self.frame3, show="headings")
        self.tree_table["columns"] = self.func.column_n[:-1]
        for column in self.func.column_n[:-1]:
            self.tree_table.column(column, minwidth= 80, width=180, stretch=True)
            self.tree_table.heading(column, text=column)

        self.scrollbar = ttk.Scrollbar(self.frame3, orient="vertical", command=self.tree_table.yview)
        self.tree_table.configure(yscrollcommand=self.scrollbar.set)

        for i, row in enumerate(self.func.users_list):
            self.tree_table.insert("", "end", text=str(i + 1), values=row)
        
        self.tree_table.pack(side="left", fill="y", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        self.tree_table.configure(height=20)

app = Interfaz()