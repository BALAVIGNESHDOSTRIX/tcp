from typing import Union

from fastapi import FastAPI
from routes.toxic import toxic_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=[
		"*"
	],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

app.include_router(toxic_router)