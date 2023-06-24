from tkinter import Tk, Frame, Label, Entry, Button

class AutomasYGramaticaApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('Autómatas y Gramática')
        self.root.geometry('1000x574')

        self.create_frames()
        self.create_widgets()

        self.root.mainloop()

    def create_frames(self):
        self.frame1 = Frame(self.root, width=1000, height=46)
        self.frame1.configure(bg='blue')
        self.frame1.pack(side='top')

        self.frame2 = Frame(self.root, width=1000, height=475)
        self.frame2.pack(side='top')

        self.frame3 = Frame(self.root, width=1000, height=46)
        self.frame3.configure(bg='blue')
        self.frame3.pack(side='top')

    def create_widgets(self):
        lbl1 = Label(self.frame1, text='Fecha de inicio:\n"AAAA-MM-DD"', font=16)
        lbl1.place(x=120, y=1, width=130, height=44)
        self.txt1 = Entry(self.frame1, bg='white', fg='black')
        self.txt1.place(x=255, y=2, width=130, height=42)

        lbl2 = Label(self.frame1, text='Fecha de finalización:\n"AAAA-MM-DD"', font=16)
        lbl2.place(x=575, y=1, width=175, height=44)
        self.txt2 = Entry(self.frame1, bg='white', fg='black')
        self.txt2.place(x=755, y=2, width=130, height=42)

    #     btn1 = Button(self.frame1, text='Cargar Datos', font=16)
    #     btn1.place(relx=0.20, rely=0.70, relwidth=0.24, relheight=0.08)

    #     btn2 = Button(self.frame1, text='Reiniciar', font=16)
    #     btn2.place(relx=0.56, rely=0.70, relwidth=0.24, relheight=0.08)

app = AutomasYGramaticaApp()
