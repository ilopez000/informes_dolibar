#https://pip.pypa.io/en/stable/installation/
#pip install mysql.connector
import mysql.connector


def consulta1():
    try:
        # Establecer la conexión con la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            port=3306,
            user='admin',
            password='adminadmin',
            database='dolibarr'
        )

        cursor = conexion.cursor()

        # Ejecutar la consulta SQL
        cursor.execute("SELECT * FROM llx_user")

        # Obtener todos los resultados
        resultados = cursor.fetchall()

        # Mostrar los resultados
        for fila in resultados:
            print(fila)

    except mysql.connector.Error as error:
        print(f"Se produjo un error: {error}")

    finally:
        if (conexion.is_connected()):
            cursor.close()
            conexion.close()
            print("La conexión a la base de datos se ha cerrado")

consulta1()
