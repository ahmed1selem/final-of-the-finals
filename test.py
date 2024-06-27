from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from responce_init import ScrapeOpsFakeBrowserHeaderAgentMiddleware
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from goose3 import Goose
import requests
from random import randint
from urllib.parse import urlencode
from BrowserInit import ScrapeOpsFakeBrowserHeaderAgentMiddlewareSL
from langdetect import detect


def get_linkes(rss):
    rss_feed_url=rss
    middleware = ScrapeOpsFakeBrowserHeaderAgentMiddleware()

    request = requests.Request('GET', rss_feed_url)

    middleware.process_request(request)

    with requests.Session() as session:
        response = session.send(request.prepare())
    soup = BeautifulSoup(response.content, 'xml')

    items = soup.find_all('item')

    links = [item.find('link').text for item in items]
    return links
urls= get_linkes("http://feeds.guardian.co.uk/theguardian/world/rss")
count=0

for url in urls:
    middleware = ScrapeOpsFakeBrowserHeaderAgentMiddleware()
    url = url

    request = requests.Request('GET', url)

    middleware.process_request(request)

    with requests.Session() as session:
        response = session.send(request.prepare())
    g = Goose()
    extract = g.extract(raw_html=response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    article_img=None

    text=extract.cleaned_text
    default_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpM_cKf_2KTpEvGShmwhzmWN7rkGRdfV8W1Q&s"


    article_img = soup.find('picture')
    if article_img:
        article_img=article_img.find("source")
        article_img = article_img['srcset']
    else:
        article_img=default_image_url
     

    count+=1
    print("*"*40)
    print(count)
    print(text,"\n tex \n", extract.title,"\n title \n",article_img)






