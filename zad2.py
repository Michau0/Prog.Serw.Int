import requests
from bs4 import BeautifulSoup

print("Podaj miasto:")
miasto = input()

url = "https://www.meteoprog.pl/pl/weather/"+miasto+"/"
response = requests.get(url)

soup = BeautifulSoup(response.content, features="html.parser" )
list = soup.find("ul", class_="today-hourly-weather hide-scroll")

for i in list:
    pora = i.find("span", class_="today-hourly-weather__name")

