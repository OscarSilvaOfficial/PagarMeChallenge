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