import pymongo
from bson.objectid import ObjectId

class ClientesModel:
    def __init__(self, uri="mongodb+srv://2124300363_db_user:Angelo20@cluster0.pmxdtim.mongodb.net/?retryWrites=true&w=majority", db_name="ecommerce", collection_name="clientes"):
        self.client = pymongo.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def agregar_cliente(self, cliente_data):
        """Agrega un nuevo cliente a la colección."""
        resultado = self.collection.insert_one(cliente_data)
        return resultado.inserted_id

    def obtener_clientes(self):
        """Obtiene todos los clientes de la colección."""
        return list(self.collection.find())

    def obtener_cliente_por_id(self, cliente_id):
        """Obtiene un cliente por su ID."""
        return self.collection.find_one({"_id": ObjectId(cliente_id)})

    def actualizar_cliente(self, cliente_id, datos_actualizados):
        """Actualiza un cliente existente."""
        resultado = self.collection.update_one(
            {"_id": ObjectId(cliente_id)},
            {"$set": datos_actualizados}
        )
        return resultado.modified_count

    def eliminar_cliente(self, cliente_id):
        """Elimina un cliente por su ID."""
        resultado = self.collection.delete_one({"_id": ObjectId(cliente_id)})
        return resultado.deleted_count

    def autenticar_cliente(self, email, password):
        """Verifica si el email y password coinciden con un cliente existente."""
        cliente = self.collection.find_one({"email": email})
        return cliente and cliente["password"] == password