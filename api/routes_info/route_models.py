from typing import Optional
from fastapi import APIRouter, HTTPException, Query
import json

router = APIRouter()


@router.get("/", status_code=201)
async def get_models(model_id: Optional[int] = Query(None)):
    f = open("./bin/json/models.json", "r")
    data = json.load(f)

    # If model_id query is None (default), return all models
    if model_id is None:
        return data

    # If data exists and model_id is not None, return the model with the given id
    if data != None:
        for model in data:
            if model["id"] == model_id:
                return model
    else:
        # If data does not exist, return 404
        raise HTTPException(
            status_code=403, detail="Given model_id is not supported"
        )