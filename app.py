from fastapi import FastAPI

app = FastAPI(title="CICD-Demo")


def add(a, b):
    return a + b


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/add")
def add_endpoint(a: int, b: int):
    return {"result": add(a, b)}
