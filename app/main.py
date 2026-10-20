from fastapi import FastAPI

app = FastAPI(title="Sensor Platform")


@app.get("/health")
def health():
    return {"status": "ok"}