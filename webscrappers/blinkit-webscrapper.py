import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# URL of the Blinkit platform or any page you want to scrape
url = 'https://blinkit.com/cn/fresh-vegetables/cid/1487/1489'
# Send an HTTP GET request to the URL
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extracting specific information (e.g., product names and prices)
    # Modify this part to extract the relevant data you need.

    # Assuming products are listed under <div class="product-name"> and <div class="price">
    products = soup.find_all("div", class_="Product__UpdatedTitle-sc-11dk8zk-9")
    prices = soup.find_all('div', style="color:rgb(31 31 31);font-weight:600;font-size:12px")
    weights = soup.find_all('span', class_="plp-product__quantity--box")

    for link in products:
        print(link.text.strip())

    for link in prices:
            print(link.text.strip())
#
    for link in weights:
#         h4_tag = link.find("h4")
        print(link.text.strip())

    # List to store data
    data = []

    for product, price , weight in zip(products, prices , weights):
        product_name = product.text.strip()  # Get product name
        product_price = price.text.strip()  # Get product price
        quantity = weight.text.strip()  # Get product quantity
        # Append the extracted data to the list
        data.append([product_name, product_price, quantity])

    # Convert the data into a DataFrame for better readability
    df = pd.DataFrame(data, columns=['Product Name', 'Price' , 'quantity'])

    # Display the data (or save it to a CSV)
    print(df)
    df.to_csv('blinkit_products.csv', index=False)  # Save to CSV

else:
    print(f"Failed to retrieve content, status code: {response.status_code}")
