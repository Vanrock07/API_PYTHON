import DBconexion
import crud
import os

user = os.environ.get("usuario_mysql")
passw = os.environ.get("pass_mysql")

con = DBconexion.CrearConexion(user, passw)

if con:
    crud.ConsultaDatos(con)
    crud.BuscarId(con)
    DBconexion.Desconectarse(con)
