import mysql.connector
import pandas as pd

# 1️⃣ Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",          # Replace with your MySQL username
    password="ayush123",  # Replace with your MySQL password
    database="sahi_price"  # Replace with your database name
)
cursor = conn.cursor()

# 2️⃣ Load Excel File
excel_file = "../scrapped_csv/blinkit_products.csv"  # Change to your actual file name
df = pd.read_csv(excel_file)

def clean_price(price):
    return float(price.replace("₹", "").strip())  # ✅ Removes ₹ and converts to float

df["Price"] = df["Price"].astype(str).apply(clean_price)  # Apply function to price column

# 3️⃣ Insert Data into MySQL
for _, row in df.iterrows():
    sql = "INSERT INTO blinkit_products (product_name, price, quantity) VALUES (%s, %s, %s)"
    values = (row["Product Name"], row["Price"], row["quantity"])  # Modify column names based on your Excel file
    cursor.execute(sql, values)

conn.commit()  # Save changes
cursor.close()
conn.close()

print("✅ Data imported successfully!")
