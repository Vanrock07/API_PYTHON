import mysql.connector   
from mysql.connector import Error #la clase error tiene la lista de errores 
import os

#conexion
def CrearConexion():
    conexion = None
    try:
        conexion = mysql.connector.connect(
                    host= 'localhost', 
                    user = 'root', 
                    password = 'root', 
                   # db = 'demo'
                   )
        if conexion:
            print ("Conexion exitosa")
            print(conexion)  
           
    except Error as e:
        conexion = None
        print ("Error al conectarse") 
        print(e)   

    return conexion
        
#Desconexion
def Desconectarse(conexion):
    
    if conexion:
        conexion.close()
        print("Desconectado")

#consulta de las bases de datos existentes
def ConsultaDatos(conexion):        
    
    cursor = conexion.cursor()
    cursor.execute('SHOW DATABASES')  #consulta todos los datos de la tabla
    
    for bd in cursor:
        print (bd)
    cursor.close()

con = CrearConexion() 

if con:
    ConsultaDatos(con)
    Desconectarse(con)







# class DataBase:
#     def _init_(self):
#         self.connection = pymysql.connect( 
#             host= 'localhost', 
#             user = 'root', 
#             password = 'root', 
#             db = 'demo'
#         )

#         self.cursor = self.connection.cursor()
#         print("Conexion establecida con la base de datos")

#     def select_user (self, id):
#         sql = 'SELECT id, username, email FROM users WHERE ID{}'.format(id)

#         try:
#             self.cursor.execute(sql)
#             user = self.cursor.fetchone()

#             print("Id", user[0])
#             print("Username", user[1])
#             print("Email", user[3])

#         except Exception as e:
#          raise    
    
# dataBase = DataBase()
# dataBase.select_user(1)