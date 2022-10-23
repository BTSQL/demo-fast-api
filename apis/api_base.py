
from fastapi import APIRouter
from apis.version1 import route_comm


api_router = APIRouter()
api_router.include_router(route_comm.router, prefix="/comm", tags=["comm"] )

#나중에 API가 추가가 되면 계속해서 붙이면 됩니다. 