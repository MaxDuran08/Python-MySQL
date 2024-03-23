from flask import Flask, jsonify
import mysql.connector
import pandas as pd
app = Flask(__name__) 

# Configuración de la conexión a la base de datos
db_config = {
    'user': 'root',
    'password': 'secret',
    'host': 'localhost',
    'database': 'pensum',
    'port': 3306,
}



# Función para establecer una conexión a la base de datos
def connect_to_database():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/api/data/crearmodelo', methods=['GET'])
def crearmodelo():

    try:
        # Establecer conexión a la base de datos
        connection = connect_to_database()
        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor(dictionary=True)
        # Definir la consulta SQL
        query = """
CREATE TABLE `pensum`.`semestre3` (
  `codigo` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Creditos` INT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`codigo`));


CREATE TABLE `pensum`.`semestre2` (
  `codigo` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Creditos` INT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`codigo`));

CREATE TABLE `pensum`.`semestre1` (
  `codigo` INT NOT NULL,
  `Nombre` VARCHAR(45) NOT NULL,
  `Creditos` INT NOT NULL,
  `Estado` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`codigo`));
         """
        # Ejecutar la consulta SQL
        cursor.execute(query)
        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()
        # Devolver el resultado en formato JSON

        return jsonify({'message': 'Modelo creado con éxito "'})

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/api/data/cargardatos', methods=['GET'])
def cargardatos():


    try:
        # Leer datos desde el archivo CSV
        df = pd.read_csv('./data/Semestre1.csv', sep=';')
        # Establecer conexión a la base de datos
        connection = connect_to_database()
        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor(dictionary=True)
        # Definir la consulta SQL
        # Insertar los datos en la tabla "paises"
        for index, row in df.iterrows():
            query = "INSERT INTO semestre1 (codigo, Nombre, Creditos, Estado) VALUES (%s, %s, %s, %s)"
            values = (row['codigo'], row['Nombre'],row['Creditos'],row['Estado'])
            cursor.execute(query, values)
    
        # Cerrar el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()
        # Devolver el resultado en formato JSON


        # Leer datos desde el archivo CSV
        df = pd.read_csv('./data/Semestre2.csv', sep=';')
        # Establecer conexión a la base de datos
        connection = connect_to_database()
        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor(dictionary=True)
        # Definir la consulta SQL
        # Insertar los datos en la tabla "paises"
        for index, row in df.iterrows():
            query = "INSERT INTO semestre2 (codigo, Nombre, Creditos, Estado) VALUES (%s, %s, %s, %s)"
            values = (row['codigo'], row['Nombre'],row['Creditos'],row['Estado'])
            cursor.execute(query, values)
    
        # Cerrar el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()
        # Devolver el resultado en formato JSON





        # Leer datos desde el archivo CSV
        df = pd.read_csv('./data/Semestre3.csv', sep=';')
        # Establecer conexión a la base de datos
        connection = connect_to_database()
        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor(dictionary=True)
        # Definir la consulta SQL
        # Insertar los datos en la tabla "paises"
        for index, row in df.iterrows():
            query = "INSERT INTO semestre3 (codigo, Nombre, Creditos, Estado) VALUES (%s, %s, %s, %s)"
            values = (row['codigo'], row['Nombre'],row['Creditos'],row['Estado'])
            cursor.execute(query, values)
  
        # Cerrar el cursor y la conexión
        connection.commit()
        cursor.close()
        connection.close()
        # Devolver el resultado en formato JSON


        return jsonify({'message': 'Datos cargados con éxito "'})

    except Exception as e:
        return jsonify({'error': str(e)})




@app.route('/api/data/consulta1', methods=['GET'])
def consulta1():
    try:

  
        # Establecer conexión a la base de datos
        connection = connect_to_database()

        # Crear un cursor para ejecutar consultas SQL
        cursor = connection.cursor(dictionary=True)

        # Definir la consulta SQL
        query = """
          
SELECT codigo, Nombre, Creditos,Estado
FROM (
    SELECT codigo, Nombre, Creditos, Estado FROM semestre1
    UNION ALL
    SELECT codigo, Nombre, Creditos, Estado FROM semestre2
    UNION ALL
    SELECT codigo, Nombre, Creditos, Estado FROM semestre3
) AS cursos_totales
WHERE Estado = 'Aprobado';
            """


        # Ejecutar la consulta SQL
        cursor.execute(query)

        # Obtener el resultado de la consulta
        result = cursor.fetchall()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        # Devolver el resultado en formato JSON
        return jsonify(result)


    except Exception as e:
        return jsonify({'error': str(e)})





if __name__ == '__main__':
    app.run(debug=True)