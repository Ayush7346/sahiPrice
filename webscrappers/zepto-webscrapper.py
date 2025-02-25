import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Zepto platform or any page you want to scrape
url = 'https://www.zepto.com/cn/fruits-vegetables/all/cid/64374cfe-d06f-4a01-898e-c07c46462c36/scid/e78a8422-5f20-4e4b-9a9f-22a0e53962e3'
# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extracting specific information (e.g., product names and prices)
    # Modify this part to extract the relevant data you need.

    # Assuming products are listed under <div class="product-name"> and <div class="price">
    products = soup.find_all('h5', {"data-testid": "product-card-name" })
    prices = soup.find_all('h4', {"data-testid": "product-card-price" })
    weights = soup.find_all('span', {"data-testid": "product-card-quantity" })

    for link in products:
        print(link.text.strip())

    for link in prices:
            print(link.text.strip())

    for link in weights:
        print(link)
        h5_tag = link.find("h5")
        print(h5_tag.text.strip())

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
    df.to_csv('../scrapped_csv/zepto_products.csv', index=False)  # Save to CSV

else:
    print(f"Failed to retrieve content, status code: {response.status_code}")
