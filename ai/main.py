# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Additional endpoint code will be added here to integrate with SAP AI Core services.