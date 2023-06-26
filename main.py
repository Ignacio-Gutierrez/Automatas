import csv
import re
import pandas as pd
from tkinter import filedialog, IntVar
from openpyxl import Workbook



class Funciones:
    def __init__(self):
        self.data_t = []
        self.data_rang = []
        self.error_rang = []
        self.column_n = ['ID',
                         'Usuario',
                         'Inicio_de_Conexión_Dia',
                         'FIN_de_Conexión_Dia',
                         'Session_Time']
        
        self.column = ['ID',
                        'ID_Sesion',
                        'ID_Conexión_unico',
                        'Usuario','IP_NAS_AP',
                        'Tipo__conexión','Inicio_de_Conexión_Dia',
                        'Inicio_de_Conexión_Hora',
                        'FIN_de_Conexión_Dia','FIN_de_Conexión_Hora',
                        'Session_Time',
                        'Input_Octects',
                        'Output_Octects',
                        'MAC_AP',
                        'MAC_Cliente',
                        'Razon_de_Terminación_de_Sesión',
                        '',
                        '']
        
        self.data_imp = IntVar()
        self.connected = IntVar()  
        self.errors = IntVar()
        self.fecha = re.compile(r"^(2019|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$")


    def import_file(self):
        data_in = filedialog.askopenfilename(title='Abrir archivo .csv', filetypes=[('Archivos CSV', '*.csv')]) 
        with open(data_in, 'r') as file:   
            reader = csv.reader(file)
            self.data_t = list(reader)

            self.data_imp.set(int(len(self.data_t)-1))


    def export_file(self):
        data_out = filedialog.asksaveasfilename(title='Guardar archivo', filetypes=[('Archivos Excel', '*.xlsx'), ('Archivos CSV', '*.csv')])
        if data_out:
            if data_out.endswith('.xlsx'):
                df = pd.DataFrame(self.data_t)
                df.to_excel(data_out, index=False)
            elif data_out.endswith('.csv'):
                with open(data_out, 'w', newline='') as output:
                    writer = csv.writer(output)
                    writer.writerows(self.data_t)

    def start(self, fecha_ini, fecha_fin):
        self.data_rang = []
        self.error_rang = []

        for row in self.data_t:
            fec_ini = row[6]
            fec_fin = row[8]

            if self.fecha.match(fec_ini) or self.fecha.match(fec_fin):
                if fecha_ini <= fec_ini <= fecha_fin or fecha_ini <= fec_fin <= fecha_fin:
                    self.data_rang.append(row)
            else:
                if fec_ini != 'Inicio_de_Conexión_Dia':
                    self.error_rang.append(row)

        self.connected.set(int(len(self.data_rang)))
        self.errors.set(int(len(self.error_rang)))

        pd.set_option('display.max_rows', None)
        df_ok = pd.DataFrame(self.data_rang, columns=self.column)
        df_ok.index += 1

        df = df_ok[self.column_n]
        print(df)

    def close(window):
        window.destroy()