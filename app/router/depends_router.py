from fastapi import APIRouter, Response, status, Depends
from router.blog import required_functionality


router = APIRouter(prefix="/depends_demo", tags = ['depends'])

@router.get("/new", summary="demo of depends functionality")
def demo_depends(req_func: dict = Depends(required_functionality)):
    return req_func