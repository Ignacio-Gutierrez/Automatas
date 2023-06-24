import csv
import re
import pandas as pd
from tkinter import filedialog


class AutomasYGramatica:
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
        
        self.data_imp = 0
        self.connected = 0  
        self.errors = 0

    def import_file():
        readed = filedialog.askopenfilename(title='Abrir archivo .csv', filetypes=[('Archivos CSV', '*.csv')]) 
        return readed
    
    def export_file():
        pass

    def start(self):
        pass

    def close(window):
        window.destroy()