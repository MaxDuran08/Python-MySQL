from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import configuracion
from diccionario import diccionario
import csv

app = Flask(__name__)
conexion = MySQL(app)

@app.route('/<string:peticion>')
def consulta(peticion):
    try:
        if peticion == 'consulta0':
            cursor=conexion.connection.cursor()
            with open('./data/paises.csv', 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=';')
                for row in csv_reader:
                    id_pais = int(row['id_pais'])
                    nombre = str(row['nombre'])
                    query = '''
                            insert into paises (id_pais, nombre) values (%s, %s);
                            '''
                    values = (id_pais, nombre)
                    cursor.execute(query, values)

            with open('./data/clientes.csv', 'r', encoding='utf-8') as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=';')
                for row in csv_reader:
                    id_cliente = int(row['id_cliente'])
                    nombre = str(row['Nombre'])
                    apellido = str(row['Apellido'])
                    direccion = str(row['Direccion'])
                    telefono = str(row['Telefono'])
                    tarjeta = str(row['Tarjeta'])
                    edad = int(row['Edad'])
                    salario = float(row['Salario'])
                    genero = str(row['Genero'])
                    id_pais = int(row['id_pais'])
                    query = '''
                            insert into clientes (id_cliente, nombre, apellido, direccion, telefono, tarjeta, edad, salario, genero, id_pais) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                            '''
                    values = (id_cliente, nombre, apellido, direccion, telefono, tarjeta, edad, salario, genero, id_pais)
                    cursor.execute(query, values)
            cursor.close()
            conexion.connection.commit()
            return jsonify({'Respuesta': 'Carga Completada'})

        else:
            cursor = conexion.connection.cursor()
            cursor.execute(diccionario[peticion])
            datos = cursor.fetchall()
            cursor.close()
            conexion.connection.commit()
            return jsonify({'Respuesta': datos})
    except Exception as e:
        return jsonify({'Respuesta':f'Error -> {e}'})

if __name__ == '__main__':
    app.config.from_object(configuracion['configuracion'])
    app.run()