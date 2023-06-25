import csv
import re
import pandas as pd

file = '/home/ignacio/Desktop/AyG/export-2019-to-now-v4.csv'

data_table = []
datos_en_rango = []
errores_en_rango = []
columnas_seleccionadas = ['ID', 'Usuario', 'Inicio_de_Conexión_Dia', 'FIN_de_Conexión_Dia', 'Session_Time']

columnas = ['ID', 'ID_Sesion', 'ID_Conexión_unico', 'Usuario', 'IP_NAS_AP',
            'Tipo__conexión', 'Inicio_de_Conexión_Dia', 'Inicio_de_Conexión_Hora',
            'FIN_de_Conexión_Dia', 'FIN_de_Conexión_Hora', 'Session_Time',
            'Input_Octects', 'Output_Octects', 'MAC_AP',
            'MAC_Cliente', 'Razon_de_Terminación_de_Sesión','','']

fecha = re.compile(r"^(2019|202[0-3])-(0[1-9]|1[0-2])-(0[1-9]|[1-2][0-9]|3[0-1])$")  # fechas que existen

fecha_ini = input('Ingresa fecha de inicio "AAAA-MM-DD": ')
fecha_fin = input('Ingresa fecha de finalización "AAAA-MM-DD": ')

with open(file, 'r') as data:
    readed = csv.reader(data)
    data_table = list(readed)

for row in data_table:
    fec_ini = row[6]
    fec_fin = row[8]

    if fecha.match(fec_ini) or fecha.match(fec_fin):
        if fecha_ini <= fec_ini <= fecha_fin or fecha_ini <= fec_fin <= fecha_fin:
            datos_en_rango.append(row)
    else:
        if fec_ini != 'Inicio_de_Conexión_Dia':
            errores_en_rango.append(row)

pd.set_option('display.max_rows', None)
df_ok = pd.DataFrame(datos_en_rango, columns=columnas)
df_ok.index += 1

df = df_ok[columnas_seleccionadas]
print(df)

num_errores = len(errores_en_rango)
print(f'Hay {num_errores} fila{"s" if num_errores != 1 else ""} con error')