import csv
import re
import pandas as pd
from tkinter import filedialog, IntVar

class Funciones:
    def __init__(self):
        self.data_t = []
        self.data_filt = []
        self.data_range = []
        self.error_range = []
        self.users_list = []
        self.dicti_users = {}

        self.column_n = ['ID',
                        'Usuario',
                        'Inicio_de_Conexión_Dia',
                        'FIN_de_Conexión_Dia',
                        'Session_Time',
                        'MAC_Cliente']
        
        self.column = ['ID',
                        'ID_Sesion',
                        'ID_Conexión_unico',
                        'Usuario',
                        'IP_NAS_AP',
                        'Tipo__conexión',
                        'Inicio_de_Conexión_Dia',
                        'Inicio_de_Conexión_Hora',
                        'FIN_de_Conexión_Dia',
                        'FIN_de_Conexión_Hora',
                        'Session_Time',
                        'Input_Octects',
                        'Output_Octects',
                        'MAC_AP',
                        'MAC_Cliente',
                        'Razon_de_Terminación_de_Sesión',
                        ]
        
        self.patterns = [
                        re.compile(r"^\d+$"),  # ID
                        re.compile(r"^(([0-9]|[A-F]){8}|([0-9]|[A-F]){16})(-([0-9]|[A-F]){8})?$"),  # ID_Sesion
                        re.compile(r"^([0-9]|[a-f]){16}$"),  # ID_Conexión_unico
                        re.compile(r"^\D+$"),  # Usuario
                        re.compile(r"^(?:\d{1,3}\.){3}\d{1,3}$"),  # IP_NAS_AP
                        re.compile(r"^Wireless-802.11$"),  # Tipo__conexión
                        re.compile(r"^(2019|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"),  # Inicio_de_Conexión_Dia
                        re.compile(r"^([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$"),  # Inicio_de_Conexión_Hora
                        re.compile(r"^(2019|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$"),  # FIN_de_Conexión_Dia
                        re.compile(r"^([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$"),  # FIN_de_Conexión_Hora
                        re.compile(r"^\d+$"),  # Session_Time
                        re.compile(r"^\d+$"),  # Input_Octects
                        re.compile(r"^\d+$"),  # Output_Octects
                        re.compile(r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}:[A-Z]{4}$"),  # MAC_AP
                        re.compile(r"^(([A-F]|[0-9]){2}-){5}([A-F]|[0-9]){2}$"),  # MAC_Cliente
                        re.compile(r"\D+|$"),  # Razon_de_Terminación_de_Sesión
                        re.compile(r"\D+|$"),
                        re.compile(r"\D+|$")
                        ]
        
        self.data_imp = IntVar()
        self.connected = IntVar()  
        self.errors = IntVar()

    def import_file(self):
        data_in = filedialog.askopenfilename(title='Abrir archivo .csv', filetypes=[('Archivos CSV', '*.csv')]) 
        with open(data_in, 'r') as file:   
            reader = csv.reader(file)
            self.data_t = list(reader)

            self.data_imp.set(int(len(self.data_t)-1))
        
        self.filter_user()

    def export_file_range(self):
        data_out = filedialog.asksaveasfilename(title='Guardar archivo', filetypes=[('Archivos Excel', '*.xlsx'), ('Archivos CSV', '*.csv')])
        if data_out:
            if data_out.endswith('.xlsx'):
                df = pd.DataFrame(self.data_range, columns=self.column)
                df.to_excel(data_out, index=False)
            elif data_out.endswith('.csv'):
                with open(data_out, 'w', newline='') as output:
                    writer = csv.writer(output)
                    writer.writerow(self.column)
                    writer.writerows(self.data_range)
    
    def export_file_error(self):
        data_out = filedialog.asksaveasfilename(title='Guardar archivo', filetypes=[('Archivos Excel', '*.xlsx'), ('Archivos CSV', '*.csv')])
        if data_out:
            if data_out.endswith('.xlsx'):
                df = pd.DataFrame(self.error_range)
                df.to_excel(data_out, index=False)
            elif data_out.endswith('.csv'):
                with open(data_out, 'w', newline='') as output:
                    writer = csv.writer(output)
                    writer.writerows(self.error_range)

    def filter_user(self):
        self.data_filt = []
        self.error_range = []

        print('Filtrando Usuarios\n')

        for row in range(len(self.data_t)):
            for col in range(len(self.data_t[row])):
                if not self.patterns[col].match(self.data_t[row][col]):
                    self.error_range.append(self.data_t[row])
                    break
            else:
                self.data_filt.append((self.data_t[row])[:-2])

        self.errors.set(int(len(self.error_range))-1)

        print('Filtrando Usuarios 2\n')

        next_user_id = 1

        for row in self.data_filt:
            user = row[3]
            date_first = row[6]
            date_last = row[8]
            session_time = int(row[10])
            user_exist = None
            
            for col in self.users_list:
                if col[1] == user:
                    user_exist = col
                    break
            
            if user_exist:
                if date_first < user_exist[2]:
                    user_exist[2] = date_first
                if date_last > user_exist[3]:
                    user_exist[3] = date_last
                else:
                    user_exist[4] += session_time
            else:
                self.users_list.append([next_user_id, user, date_first, date_last, session_time])
                next_user_id += 1

        pd.set_option('display.max_rows', None)
        df = pd.DataFrame(self.users_list, columns=self.column_n[:-1])

        print(df.to_string(index=False))

        for u in self.users_list:
            user_id = u[0]
            user = u[1]
            self.dicti_users[user_id] = user
        
    def start(self, name_user, fecha_ini, fecha_fin):
        self.data_range = []

        print('Procesando SOLICITUD')

        if self.patterns[6].match(fecha_ini) and self.patterns[8].match(fecha_fin):
            if fecha_ini <= fecha_fin:
                if self.patterns[3].match(name_user):
                    for row in self.data_filt:
                        if fecha_ini <= row[6] <= fecha_fin or fecha_ini <= row[6] <= fecha_fin:
                            if name_user == row[3]:
                                self.data_range.append(row)
                elif self.patterns[0].match(name_user):
                    for row in self.data_filt:
                        if fecha_ini <= row[6] <= fecha_fin or fecha_ini <= row[6] <= fecha_fin:
                            if self.dicti_users[int(name_user)] == row[3]:
                                self.data_range.append(row)
                else:
                    print(f'{name_user} no es válido.')
            else:
                print('El periodo de fechas no es correcto.')
        else:
            print('La fecha ingresada no está en un formato válido.')

        self.connected.set(int(len(self.data_range)))        

        if self.data_range:
            pd.set_option('display.max_rows', None)
            df = pd.DataFrame(self.data_range, columns=self.column)
            df = df[self.column_n[:-1]]
            print(df.to_string(index=False))
        else:
            print('No hay datos')

    def close(window):
        window.destroy()