#pip install pandas xlsxwriter openpyxl mysql-connector-python
import mysql.connector
import pandas as pd

def consulta2():
    try:
        # Establecer la conexión con la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='root',
            password='changeme',
            database='dolibarr'
        )

        cursor = conexion.cursor()

        # Ejecutar la consulta SQL
        cursor.execute("SELECT * FROM llx_user")

        # Obtener todos los resultados en un DataFrame de Pandas
        resultados = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

        # Guardar el DataFrame en un archivo Excel
        nombre_archivo = "resultados_consulta.xlsx"
        # Puedes usar el engine 'xlsxwriter' o 'openpyxl'. Aquí se usa 'openpyxl'
        resultados.to_excel(nombre_archivo, index=False, engine='openpyxl')

        print(f"Los resultados se han guardado en el archivo {nombre_archivo}")

    except mysql.connector.Error as error:
        print(f"Se produjo un error: {error}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("La conexión a la base de datos se ha cerrado")

consulta2()
