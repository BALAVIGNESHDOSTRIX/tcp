from fastapi import FastAPI, Query, File, Header, Depends, UploadFile, Body, Form
from fastapi import APIRouter
from typing import *

import requests
from models.toxic_model import ToxicOutModel, ToxicInput
from kw_src.toxic_predictor import TSensePredict, text_vectors
import time 
toxic_router = APIRouter()
import numpy as np
import urllib.parse

@toxic_router.post("/toxic_sensify", response_model=ToxicOutModel, tags=["Toxic Predictor"])
async def TextToxicfy(data: ToxicInput = None):
    request_data = data.dict() 
    pr_result = ""
    try:
        vector = text_vectors(request_data.get('text_data'))
        res = TSensePredict(np.expand_dims(vector,0))
        pr_result = (res > 0.5).astype(int)[0][0]
    except Exception as e:
        pr_result = str(e)
    return {'value': str(pr_result)}

@toxic_router.get('/testify')
async def testifykData(extattr: Optional[List[str]] = Query(...)):
    print(extattr)
    return {'value': 'Testify cool'}


# @toxic_router.get('/testify_v1')
# async def testifyData(extattr: Optional[List[str]] = Query(...)):
#     query = {}
#     r = requests.get('http://127.0.0.1:8000/testify', params=urllib.parse.urlencode({'extattr': extattr}))
#     print(r.json())
#     return {'value': 'Testify cool'}