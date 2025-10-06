from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_products():
    try:
        # Try local file first, then fallback to relative path
        try:
            with open("products.json", "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            with open("../products.json", "r", encoding="utf-8") as file:
                return json.load(file)
    except:
        return []

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/products")
def get_products():
    products = load_products()
    gold_price = 60.0  # Default gold price
    
    for product in products:
        # Calculate price: (popularityScore + 1) * weight * goldPrice
        product["price"] = round((product["popularityScore"] + 1) * product["weight"] * gold_price, 2)
        product["popularityScoreOutOf5"] = round(product["popularityScore"] * 5, 1)
    
    return products

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
