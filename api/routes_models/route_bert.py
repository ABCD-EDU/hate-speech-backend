from fastapi import APIRouter, HTTPException
import json

import loader.bert as bert

router = APIRouter()

@router.get("/")
async def get_results(message: str):
    return bert.get_result(message)