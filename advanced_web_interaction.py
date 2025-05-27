import requests

url = "https://www.example.com"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
    print(f"Successfully accessed {url}")
    print(response.text[:100]) # Print the first 100 characters of the response
except requests.exceptions.RequestException as e:
    print(f"Error accessing {url}: {e}")