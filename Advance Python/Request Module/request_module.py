# -------------------------------
# 1. Simple GET request
# -------------------------------
import requests

# Send a GET request to a test API endpoint
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

# Print HTTP status code (200 means success)
print(response.status_code)  

# Print raw response as text
print(response.text)

# Print response as JSON (dictionary)
print(response.json())       

# -------------------------------
# 2. POST request with JSON data
# -------------------------------
# import requests

# Data to send in the request body
# data = {"name": "Nitesh", "email": "nitesh@example.com"}

# Send POST request with JSON data
# response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)

# Print HTTP status code (201 means created)
# print(response.status_code)  

# Print response data (JSON)
# print(response.json())       

# -------------------------------
# 3. GET request with headers
# -------------------------------
# import requests

# Example of custom headers (e.g., Authorization token)
# headers = {"Authorization": "Bearer your_token_here"}

# Send GET request with headers
# response = requests.get("https://api.example.com/data", headers=headers)

# -------------------------------
# 4. GET request with query parameters
# -------------------------------
# import requests

# Query parameters for filtering results
# params = {"userId": 1}

# Send GET request with params (e.g., ?userId=1)
# response = requests.get("https://jsonplaceholder.typicode.com/posts", params=params)

# Print response as JSON (filtered results)
# print(response.json())

# -------------------------------
# 5. Handling errors / exceptions
# -------------------------------
# import requests

# Try-except to handle HTTP errors or other request exceptions
# try:
#     response = requests.get("https://jsonplaceholder.typicode.com/invalid")
#     response.raise_for_status()  # Raises error for bad responses (4xx, 5xx)
# except requests.exceptions.HTTPError as err:
#     print("HTTP Error:", err)
# except requests.exceptions.RequestException as err:
#     print("Other Error:", err)

# -------------------------------
# 6. Looping through JSON data from API
# -------------------------------
# import requests

# URL to fetch all users
# url = "https://jsonplaceholder.typicode.com/users"
# response = requests.get(url)
# users = response.json()  # Convert JSON response to Python dictionary/list

# Loop through each user and print details
# for user in users:
#     print(user["name"], "-", user["email"])  # Print name and email
#     print("Address:", user["address"]["street"], user["address"]["city"])  # Print address
