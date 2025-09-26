from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import uvicorn
 
load_dotenv()
 
port = int(os.getenv("PORT", 3030))
 
app = FastAPI()
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["GET"], 
    allow_headers=["*"],   
)
 
@app.get("/products")
def get_products():
    return [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=port)
 