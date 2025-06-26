from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import requests

app = FastAPI()

# OAuth2 scheme for xsuaa security
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/predict")
async def predict(token: str = Depends(oauth2_scheme)):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get("https://ai-core.example.com/predict", headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.()  # Corrected response handling
    except requests.exceptions.RequestException as e:
        # Improved error handling
        raise HTTPException(status_code=500, detail=str(e))
