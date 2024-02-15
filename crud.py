import DBconexion

#consulta de las bases de datos existentes
def ConsultaDatos(conexion):        
    
    cursor = conexion.cursor()
    cursor.execute('SHOW DATABASES')  #consulta todos los datos de la tabla
    
    for bd in cursor:
        print (bd)

    cursor.close()

# buscar por ID
def BuscarId(conexion):

    cursor = conexion.cursor()

    try:
        cursor.execute('SELECT * FROM users')
        user = cursor.fetchone()

        print("Id", user[0])
        print("Username", user[1])
        print("Email", user[2])
        
    except Exception as e:
        print("Registo no encontrado")
        raise
    finally: 
        cursor.close()   
    
    #insertar los datos
        
    