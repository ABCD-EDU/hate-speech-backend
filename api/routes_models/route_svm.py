from fastapi import APIRouter, HTTPException, Query
import json
from typing import Optional, List

import loader.svm as svm

router = APIRouter()

@router.get("/")
async def get_results(message: str, task_ids: Optional[List[int]] = Query(None)):
    if task_ids is None:
        task_ids = [1, 2, 3]
        
    return svm.get_result(message, task_ids)
    