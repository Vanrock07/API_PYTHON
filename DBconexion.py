import mysql.connector   
from mysql.connector import Error #la clase error tiene la lista de errores 
import os

#conexion
conexion = None
try:
    conexion = mysql.connector.connect(
                    host= 'localhost', 
                    user = 'root', 
                    password = 'root', )
                  #  db = 'demo'
    if conexion:
            print ("Conexion exitosa")
            print(conexion)

except Error as e:
        print ("Error al conectarse") 
        print(e)   

#consulta     
cursor = conexion.cursor()
cursor.execute("show databases")  #consulta todos los datos de la tabla
    
for bd in cursor:
    print (bd)
cursor.close()

#Desconexion
if conexion:
    conexion.close()
    print("Conexion finalizada")


