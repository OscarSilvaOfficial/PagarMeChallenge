from api.infra.http.interfaces.http_api_interface import HttpApiInterface


def main_routes(router: HttpApiInterface):
  
  @router.get('/')
  async def index():
    return {'message': 'Hello World'}
  
  return router
