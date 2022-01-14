# from sqlmodel.main import SQLModel
from .interfaces.sql_interface import DatabaseInterface
from sqlmodel import  Session, create_engine, select, SQLModel


class SQLite(DatabaseInterface):
  
  def __init__(self, entity):
    self._entity = entity
    self._session = self._session_start()
    SQLModel.metadata.create_all(self._session)
    
  def _session_start(self):
    return create_engine("sqlite:///database.db")
    
  def all(self):
    with Session(self._session) as session:
      statement = select(self._entity)
      return session.exec(statement).fetchall()
  
  def get(self, id: int):
    with Session(self._session) as session:
      statement = select(self._entity).where(self._entity.id == id)
      return session.exec(statement).first()
  
  def create(self, entity):
    with Session(self._session) as session:
      session.add(entity)
      session.commit()
      return entity
  
  def update(self, id: int, entity):
    with Session(self._session) as session:
      updated_entity = self.get(id)(**entity)
      session.add(updated_entity)
      session.commit()
      return updated_entity
    
  def delete(self, id: int):
     with Session(self._session) as session:
       entity = session.delete(self.get(id))
       session.delete(entity)
       return {'message': 'Deleted'}