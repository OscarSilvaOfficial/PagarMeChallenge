from api.adapters.controller.routes import main_routes
from fastapi import APIRouter as FastAPIRouter
from fastapi import FastAPI as FastAPIFramework

app = FastAPIFramework()
index_route = main_routes(router=FastAPIRouter())

app.include_router(index_route)