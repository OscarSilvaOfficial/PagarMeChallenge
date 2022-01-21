from api.infra.db.interfaces.sql_interface import DatabaseInterface
from api.infra.http.interfaces.http_api_interface import HttpApiInterface


def index_routes(router: HttpApiInterface, db: DatabaseInterface, response):
    
  @router.get('/')
  async def index():
    return {'message': 'Hello World'}
 