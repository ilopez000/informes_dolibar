
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
        cursor.execute("SELECT debit, credit, montant FROM llx_accounting_bookkeeping")

        # Obtener todos los resultados en un DataFrame de Pandas
        resultados = pd.DataFrame(cursor.fetchall(), columns=[i[0] for i in cursor.description])

        # Calcular el sumatorio de las columnas
        sumatorios = resultados.sum(numeric_only=True)

        # Crear un DataFrame para la fila de sumatorios
        fila_sumatorios = pd.DataFrame([sumatorios], index=['Sumatorio'])

        # Concatenar el DataFrame original con la fila de sumatorios
        resultados_con_sumatorios = pd.concat([resultados, fila_sumatorios], ignore_index=True)

        # Guardar el DataFrame en un archivo Excel
        nombre_archivo = "resultados_consulta.xlsx"
        resultados_con_sumatorios.to_excel(nombre_archivo, index=False, engine='openpyxl')

        print(f"Los resultados se han guardado en el archivo {nombre_archivo}")

    except mysql.connector.Error as error:
        print(f"Se produjo un error: {error}")

    finally:
        if conexion.is_connected():
            cursor.close()
            conexion.close()
            print("La conexión a la base de datos se ha cerrado")
