from api.infra.http.interfaces.http_api_interface import HttpApiInterface
from api.adapters.controller.accounts.routes import account_routes
from api.adapters.controller.main.routes import index_routes
from api.infra.db.interfaces.sql_interface import DatabaseInterface
from fastapi import Response


def main_routes(router: HttpApiInterface, db: DatabaseInterface, response=Response):

  all_routers = [account_routes, index_routes]
    
  for route in all_routers:
    route(router=router, db=db, response=response)
  
  return router
