### backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from backend.embedder import load_faiss_index, search_catalog

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "SHL Recommender API is live!"}

@app.on_event("startup")
def on_startup():
    load_faiss_index()

@app.post("/recommend")
def recommend(req: QueryRequest):
    return search_catalog(req.query)