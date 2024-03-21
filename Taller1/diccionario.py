class Diccionario():
    consulta1 = '''

                create table paises(
                  id_pais integer,
                  nombre varchar(50) not null,
                  constraint id_pais_pk primary key (id_pais)
                );
    
                create table clientes(
                    id_cliente integer,
                    nombre varchar(50) not null,
                    apellido varchar(50) not null,
                    direccion varchar(50) not null,
                    telefono varchar(50) not null,
                    tarjeta varchar(50) not null,
                    edad integer not null,
                    salario float(2) not null,
                    genero varchar(50) not null,
                    id_pais integer not null,
                    constraint id_cliente_pk primary key (id_cliente),
                    constraint clientes_id_pais_fk foreign key (id_pais) references paises (id_pais)
                );
                '''
    consulta2 = '''
                select nombre, apellido, edad from clientes;
                '''
    consulta3 = '''
                select id_pais, nombre from paises;
                '''
    consulta4 = '''
                select concat(c.nombre, ' ', c.apellido) as nombre_completo, c.edad, p.nombre
                from clientes c
                join paises p on p.id_pais = c.id_pais
                where p.nombre = 'Alemania' order by c.edad asc;
                '''
    consulta5 = '''
                select c.id_cliente ,concat(c.nombre, ' ', c.apellido) as nombre_completo, c.edad, c.genero, p.nombre 
                from clientes c 
                join paises p on p.id_pais = c.id_pais 
                where c.genero = 'M' and c.edad >= 18 and c.edad <= 30;
                '''
    

diccionario = {
    'consulta1' : Diccionario.consulta1,
    'consulta2' : Diccionario.consulta2,
    'consulta3' : Diccionario.consulta3,
    'consulta4' : Diccionario.consulta4,
    'consulta5' : Diccionario.consulta5,
}