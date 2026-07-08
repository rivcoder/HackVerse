from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/")
def home():
    return {"message": "PipelineGuardian API Running"}
    with open("results.json", "r") as f:
        return json.load(f)