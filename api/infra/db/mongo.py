from .interfaces.nosql_interface import NoSQLInterface
from fast_nosql_manager.implementations.mongo import MongoRepository
from api.infra.db.configs.tables_config import collections

class Mongo(NoSQLInterface):
  
  def __init__(self, db_name, mongo_string_connection):
    self._db: MongoRepository = MongoRepository(db_str_connection=mongo_string_connection, db_name=db_name)
    self._init_db()
    
  def _init_db(self):
    for collection in collections:
      self._db.create_collection(collection_name=collection)
      
  def all(self, collection_name, where={}):
    return self._db.select_all(collection_name=collection_name, where=where)
  
  def create(self, collection_name, documents):
    try:
      self._db.create_document(collection_name=collection_name, documents=documents)
    except Exception:
      return Exception('Erro ao criar')
  
  def update(self, collection_name, where, new_values):
    try:
      return self._db.update_document(collection_name=collection_name, where=where, new_values=new_values)
    except Exception:
      return Exception('Erro ao atualizar')
    
  def delete(self, collection_name, where):
    return self._db.delete_document(collection_name=collection_name, where=where)