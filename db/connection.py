from pymongo import MongoClient

def get_database():
    """
    Retorna la conexión a la base de datos de MongoDB.
    """
    client = MongoClient('mongodb://localhost:27017/')  # Cambia la URL si usas otro host o puerto
    return client.basketball_db  # Nombre de la base de datos