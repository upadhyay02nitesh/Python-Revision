import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "http://books.toscrape.com/"

# Send GET request
response = requests.get(url)
print(response.status_code)
# print(response.text)

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find all product containers
books = soup.find_all('article', class_='product_pod')

# Loop through each book and extract details
for book in books:
    # Book title
    title = book.h3.a['title']
    
    # Book price
    price = book.find('p', class_='price_color').text
    
    # Availability
    availability = book.find('p', class_='instock availability').text.strip()
    
    # Print book info
    print(f"Title: {title}")
    print(f"Price: {price}")
    print(f"Availability: {availability}")
    print("-" * 40)
