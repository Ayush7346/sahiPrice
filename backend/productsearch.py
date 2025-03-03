from fastapi import FastAPI, Query
import mysql.connector

app = FastAPI()

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="ayush123",
    database="sahi_price"
)
cursor = db.cursor(dictionary=True)

# API to fetch products based on search query
@app.get("/search/")
def search_products(q: str = Query(..., min_length=2, description="Search term")):
    print('Reached')
    query = "SELECT * FROM sahi_price.blinkit_products WHERE product_name LIKE %s"
    print(q)
    cursor.execute(query, (f"%{q}%",))
    results = cursor.fetchall()
    return {"products": results}

# Run using: uvicorn filename:app --reload
