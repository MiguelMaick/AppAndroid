'Sirve para comprobar que haga conexión con MongoDB'

from clientes_model import ClientesModel

modelo = ClientesModel()
print("Colecciones disponibles:", modelo.db.list_collection_names())