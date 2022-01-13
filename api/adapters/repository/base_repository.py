from api.infra.db.interfaces.sql_interface import DatabaseInterface


class Repository:
  
  def __init__(self, entity, db: DatabaseInterface): 
    self.db = db(entity)