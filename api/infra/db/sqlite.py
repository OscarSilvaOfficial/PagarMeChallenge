from .interfaces.sql_interface import DatabaseInterface
from fast_sql_manager.implementations.sqlite import SQLiteRepository

class SQLite(DatabaseInterface):
  
  def __init__(self, entity, db_name):
    self._db = SQLiteRepository(db_path=db_name)
    self._entity = entity

  def all(self):
    return self._db.select_all(table_name=self._entity.__name__)
  
  def get(self, id: int):
    return self._db.select_all(where={ 'id': id })
  
  def create(self, entity):
    return self._db.insert(
      table_name=self._entity.__name__,
      insert_values=entity.__dict__,
      table_columns=self._entity.__dict__
    )
  
  def update(self, id: int, entity):
    pass
    
  def delete(self, id: int):
    pass