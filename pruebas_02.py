import csv
import re
import pandas as pd

file = '/home/ignacio/Desktop/Automatas_y_Gramatica/pruebas_mal_caso.csv'

data_table = []
datos_en_rango = []
errores_en_rango = []
columnas_seleccionadas = ['ID','Usuario','Inicio_de_Conexión_Dia','FIN_de_Conexión_Dia','Session_Time']

columnas = ['ID','ID_Sesion','ID_Conexión_unico','Usuario','IP_NAS_AP',
            'Tipo__conexión','Inicio_de_Conexión_Dia','Inicio_de_Conexión_Hora',
            'FIN_de_Conexión_Dia','FIN_de_Conexión_Hora','Session_Time',
            'Input_Octects','Output_Octects','MAC_AP',
            'MAC_Cliente','Razon_de_Terminación_de_Sesión','','']

with open(file, 'r') as data:
    readed = csv.reader(data)

    for file in readed:
        data_file = file
        data_table.append(data_file)


fecha = re.compile(r"^(2019|202[0-3])([-])(0[1-9]|1[0-2])([-])(0[1-9]|[1-2][0-9]|3[0-1])$")    #fechas que existen 


fecha_ini = input('Ingresa fecha de inicio "AAAA-MM-DD": ')
fecha_fin = input('Ingresa fecha de finalización "AAAA-MM-DD": ')

for i in data_table:
    fila = data_table.index(i)

    fec_ini = data_table[fila][6]
    fec_fin = data_table[fila][8]    

    if fecha.match(fec_ini) or fecha.match(fec_fin):
        if (fecha_ini <= fec_ini <= fecha_fin) or (fecha_ini <= fec_fin <= fecha_fin):
            datos_en_rango.append(i)
    else:
        if fec_ini == 'Inicio_de_Conexión_Dia':
            pass
        else:
            errores_en_rango.append(i)

df_ok = pd.DataFrame(datos_en_rango, columns=['ID','ID_Sesion','ID_Conexión_unico','Usuario','IP_NAS_AP',
                                           'Tipo__conexión','Inicio_de_Conexión_Dia','Inicio_de_Conexión_Hora',
                                           'FIN_de_Conexión_Dia','FIN_de_Conexión_Hora','Session_Time',
                                           'Input_Octects','Output_Octects','MAC_AP',
                                           'MAC_Cliente','Razon_de_Terminación_de_Sesión','',''])
df_ok.index += 1

df = df_ok[columnas_seleccionadas]
print(df)

print(f'Hay {len(errores_en_rango)} filas con errores')