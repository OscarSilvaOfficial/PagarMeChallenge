from api.adapters.controller.routes import main_routes
from api.infra.config.env import NOSQL_DB_HOST
from api.infra.db.mongo import Mongo
from fastapi import APIRouter as FastAPIRouter
from fastapi import FastAPI as FastAPIFramework

class Entrypoint():

  db = Mongo(db_name='pagarme', mongo_string_connection=NOSQL_DB_HOST)
  app = FastAPIFramework()
  
  def mount_routes(self):
    index_route = main_routes(router=FastAPIRouter(), db=self.db)
    self.app.include_router(index_route)
  
  @staticmethod
  def factory():
    entrypoint = Entrypoint() 
    entrypoint.mount_routes()
    return entrypoint.app
  