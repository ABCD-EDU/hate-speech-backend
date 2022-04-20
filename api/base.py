from api.routes_info import route_models
from api.routes_models import route_bert
from api.routes_models import route_svm
from fastapi import APIRouter

app_router = APIRouter()

app_router.include_router(route_models.router, prefix="/models", tags=["models"])
app_router.include_router(route_bert.router, prefix="/models/bert", tags=["models"])
app_router.include_router(route_svm.router, prefix="/models/svm", tags=["models"])
