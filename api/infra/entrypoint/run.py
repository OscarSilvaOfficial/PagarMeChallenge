from api.adapters.controller.routes import main_routes
from api.entities.account.account import Account
from api.infra.db.sqlite import SQLite
from fastapi import APIRouter as FastAPIRouter
from fastapi import FastAPI as FastAPIFramework

class Entrypoint():

  db = SQLite(db_name='test.db', entity=Account)
  app = FastAPIFramework()
  
  def mount_routes(self):
    index_route = main_routes(router=FastAPIRouter(prefix='/api'), db=self.db)
    self.app.include_router(index_route)
  
  @staticmethod
  def factory():
    entrypoint = Entrypoint() 
    entrypoint.mount_routes()
    return entrypoint.app
  