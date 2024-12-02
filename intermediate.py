import requests
from bs4 import BeautifulSoup

# Step 1: Send a request to the website
url = "https://en.wikipedia.org/wiki/History"
response = requests.get(url)

# Step 2: Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Step 3: Extract data
titles = soup.find_all('h1')  # Example: Extract all <h1> tags
for title in titles:
    print(title.text)


