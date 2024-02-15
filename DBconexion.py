import mysql.connector   
from mysql.connector import Error #la clase error tiene la lista de errores 

#conexion
def CrearConexion(usuario, passw):
    conexion = None
    try:
        conexion = mysql.connector.connect(
                    host= 'localhost', 
                    user = usuario, 
                    password = passw, 
                    db = 'demo'
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


