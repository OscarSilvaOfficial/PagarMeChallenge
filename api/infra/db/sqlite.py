from dataclasses import replace
from .interfaces.sql_interface import DatabaseInterface
from fast_sql_manager.implementations.sqlite import SQLiteRepository
from api.infra.db.configs.tables_config import tables

class SQLite(DatabaseInterface):
  
  def __init__(self, entity=None, db_name=None):
    self._db = SQLiteRepository(db_path=db_name)
    self._entity = entity
    
  def _create_tables(self):
    for table in tables:
      self._db.create_table(**table)
      
  def _get_keys(self, entity):
    response = []
    for key in entity.keys():
      if key != 'validator':
        response.append(key[1:])      
    return response

  def _get_values(self, entity):
    response = []
    for value in entity.values():
      if type(value) == int or type(value) == str :
        response.append(value)
    return tuple(response)

  def all(self):
    return self._db.select_all(table_name=self._entity.__name__)
  
  def get(self, id: int=None, field: dict=None):
    if field:
      return self._db.select_all(table_name=self._entity.__name__, where=field)
    return self._db.select_all(table_name=self._entity.__name__, where={ 'id': id })
  
  def create(self, entity: object):
    entity_dict = dict(entity.__dict__)
    
    if '_id' in entity_dict:
      del entity_dict['_id']
      
    table_name = str(entity.__class__.__name__)
    insert_keys = list(self._get_keys(entity_dict))
    insert_values = tuple(self._get_values(entity_dict))
    
    return self._db.insert(
      table_name=table_name,
      insert_values=insert_values,
      table_columns=insert_keys
    )
  
  def update(self, id: int, entity):
    pass
    
  def delete(self, id: int):
    pass