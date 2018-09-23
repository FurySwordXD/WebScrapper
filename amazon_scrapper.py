from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

def scrape(product):

    asin_list = []
    scrape_url = "https://www.amazon.in/"

    webpage = urlopen(scrape_url + "s?keywords=" + str(product))
    html_data = BeautifulSoup(webpage.read(), "html.parser")
    webpage.close()
    containers = html_data.findAll("li", {"class": "s-result-item"})

    for container in containers:
        try:
            asin = container["data-asin"]
            if "ACS" in asin:
                continue
            name = container.h2.text.strip()
            price = container.findAll("span", {"class": "s-price"})[0].text.strip()
            price = price.split("-")
            price = " ".join(price)
            asin_list.append(asin)
            print(asin+": "+name+" "+price)
        except:
            continue