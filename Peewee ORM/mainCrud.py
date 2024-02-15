from paquetes.DAO.Conexion import *
from paquetes.objetos.base import *
from paquetes.objetos.usuarios import *

#crear registros
with database:
   database.create_tables([Usuario])
print("Tabla creada")  

# with database:
#    usuario1 = Usuario.create(nombre = "Juan Prado", email = "J.prado@usuarios")
#    usuario2 = Usuario.create(nombre = "Miguel Pinilla", email = "M.Pinilla@usuarios")
#    usuario3 = Usuario.create(nombre = "David Arciniegas", email = "d.arciniegas@usuarios")

#seleccionar todos los registros
with database:
    Usuario.lista()
    
 #seleccionar un registro      
with database:
     query = Usuario.get(Usuario.id == 3 )  
     print(query.id, query.nombre, query.email, query.fecha_de_creacion)
                



