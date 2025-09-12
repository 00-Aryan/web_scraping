import requests
from bs4 import BeautifulSoup
import base64


def fetch_base_url():
    url_get = 'https://hcraj.nic.in/cishcraj-jdp/JudgementFilters/'


    # url_post = 'https://hcraj.nic.in/cishcraj-jdp/judgement-filters/getrecord'

    base_url = requests.get(url_get)


    with open('base_url.html' , 'w' ,encoding="utf-8") as f:
        f.write(base_url.text)
    print("file created as base_url.html")

if __name__ == "__main__":
    fetch_url()

