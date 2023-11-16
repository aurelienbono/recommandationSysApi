from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    text: str

# Define the app
app = FastAPI(
    title="MyApp",
    description="Hello API developer!",
    version="0.1.0"
)

# Define a GET operation
@app.get("/")
async def main():
    return {"message": "Hello World "}

