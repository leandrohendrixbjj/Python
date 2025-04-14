from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
def index():
    return {"message":"Welcome to FastApi"}