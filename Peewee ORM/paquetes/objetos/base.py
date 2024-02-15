from peewee import *
from paquetes.DAO.Conexion import *

class ModeloBase(Model):
    class Meta:
        order_by = id 
