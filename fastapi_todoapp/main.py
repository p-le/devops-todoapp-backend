import os
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi_todoapp.routers import task

app = FastAPI()

origins = [
    os.getenv("UI_ORIGIN", "http://localhost:3000")
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

app.include_router(task.router)

@app.get('/healthz', status_code=status.HTTP_200_OK)
def healthz():
    return {'status': 'OK'}