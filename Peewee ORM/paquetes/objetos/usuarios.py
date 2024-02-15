from peewee import *
from paquetes.DAO.Conexion import *
from paquetes.objetos.base import *

import datetime

#Creacion de una clase con los atributos que formaran las columnas de la tabla
class Usuario(ModeloBase):
    id = AutoField(primary_key=True)
    nombre = CharField(null=True, max_length=50)
    email = CharField(null = True, max_length=80)
    fecha_de_creacion = DateField(default=datetime.datetime.now)

    @staticmethod
    def lista():
        query = Usuario.select()
        for fila in query:
            print(fila.id, fila.nombre, fila.email, fila.fecha_de_creacion)

            #Meta se usa para especificar la configuracion de la base de datos
            #se crea para cada clase/tabla que se necesite
    class Meta:
        database = database   #define la conexion
        db_table = "usuarios"   #define el nombre de la tabla  
    
    #Crea la tabla con los atributos de la clase User
# if not Usuario.table_exists(): 
#     Usuario.create_table([Usuario])        
    # User = Usuario.create()
    # return User