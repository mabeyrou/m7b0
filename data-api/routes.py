from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter()


@router.get("/")
async def home():
    return {"message": "The server is up and running!"}


@router.get("/health")
async def heath():
    return {"status": "ok"}
