from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI(title="cicd-demo")

INDEX_FILE = Path(__file__).parent / "static" / "index.html"


def add(a, b):
    return a + b


@app.get("/")
def index():
    return FileResponse(INDEX_FILE)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/add")
def add_endpoint(a: int, b: int):
    return {"result": add(a, b)}
