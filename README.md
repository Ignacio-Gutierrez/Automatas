# Automatas

Explicación del Proyecto - Análisis de Datos, centrado en la duración de sesiones

. Requisitos del sistema:
   - Python 3.x instalado en el sistema.
   - Librerías necesarias:
                           - csv: Usada para poder maneaar archivos '.csv'.
                           - re:Usada para poder trabajar con expresiones regulares.
                           - pandas:Usada para poder exportar archivos '.xlsx'.
                           - tkinter: Usada para crear la interfaz gráfica y su uso.
   - Instaciones necesarias:
                            - pip install pandas
                            - sudo apt-get install python3-tk
                            - pip install openpyxl

. Descripción general:
   El código es una aplicación de análisis de datos que permite importar archivos CSV, filtrar y analizar los datos, y exportar los resultados en formatos de archivo Excel o CSV. 
   La aplicación utiliza una interfaz gráfica de usuario realizada con la biblioteca Tkinter.


. Manual de Usuario:

    1. Importar archivo CSV:
        - Hacer clic en el botón "Importar" para seleccionar un archivo CSV que contenga los datos que se desean analizar.
        - Se abrirá una ventana para seleccionar el archivo CSV.
        - Una vez seleccionado el archivo, los datos se cargarán en la aplicación y se mostrarán en una tabla, que contendrá un ID, Usuario, Primer fecha de acceso, Última fecha de acceso y el tiempo total de sesión de cada usuario.

    2. Filtrar datos por usuario y rango de fechas:
        - Ingresar el nombre de usuario o su id en el campo "Usuario 'ID | Usuario'".
        - Ingresar la fecha de inicio en el campo "Fecha de inicio 'AAAA-MM-DD'" en el formato "AAAA-MM-DD".
        - Ingresar la fecha de fin en el campo "Fecha de fin 'AAAA-MM-DD'" en el formato "AAAA-MM-DD".
        - Hacer clic en el botón "Iniciar" para filtrar los datos.
        - Los datos filtrados se mostrarán en una tabla que contendrá un ID(en la red), Usuario, Primer fecha de acceso, Última fecha de acceso y el tiempo de sesión de cada registro, y la MAC del usuario.

    3. Exportar datos filtrados:
        - Hacer clic en el botón "Exportar" para guardar los datos filtrados en un archivo Excel o CSV.
        - Se abrirá una ventana para seleccionar la ubicación y el nombre del archivo de salida.
        - Elegir el formato de archivo deseado en el menú desplegable de la ventana y hacer clic en "Guardar" para completar la exportación.

    4. Exportar errores:
        - Hacer clic en el botón "Exportar Errores" para guardar los registros que contienen errores de formato en un archivo Excel o CSV.
        - Se abrirá una ventana para seleccionar la ubicación y el nombre del archivo de salida.
        - Eligir el formato de archivo deseado en el menú desplegable de la ventana y hacer clic en "Guardar" para completar la exportación.

    5. Información adicional:
        - En la parte inferior de la ventana, se muestra información sobre los datos importados, el número de conexiones en el periodo establecido y el número de errores encontrados en el archivo importado.
        - Hacer clic en el botón "Salir" para cerrar la aplicación.

Intengrantes:
    - Camila Portal
    - Ignacio de Luca
    - Luciano Faraz
    - Ignacio Gutierrez 
