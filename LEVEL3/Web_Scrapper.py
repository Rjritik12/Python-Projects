import requests
from bs4 import BeautifulSoup

url = input("Enter the URL:")
req =  requests.get(url)
Soup = BeautifulSoup(req.content,"html.parser" )
print(Soup.prettify())