
from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
import urllib
import shutil
import re
import ssl
import random
import secrets
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

urls = []
#page = requests.get("https://owllife.kennesaw.edu/event/1482150")
driver = webdriver.Chrome("path to driver")
driver.get("website link")
html = driver.page_source
soup = BeautifulSoup(html, "html5lib")
description = soup.find("div", attrs={"class":"DescriptionText"}).getText()
eventName = soup.find("h1", attrs={"style": "padding: 0px;"}).getText()
organization = soup.find("h3", attrs={"style": "margin: 20px 0px 31px;"}).getText()
time = soup.find("p", attrs={"style": "margin: 0px; padding-left: 33px; text-decoration: none;"}).getText()
locationName = soup.find_all("p", attrs={"style": "margin: 0px;"})
img = soup.find("div", attrs={"style": "margin: 10px 30px 10px 10px; flex: 1 1 0%;"}).find("background-image")
for ele in soup.find_all('div', attrs={'style':'margin: 10px 30px 10px 10px; flex: 1 1 0%;'}):
    pattern = re.compile('.*background-image:\s*url\((.*)\);')
    match = pattern.match(ele.div['style'])
    if match:
        urls.append(match.group(1))
print(urls[0].replace('"', ''))

r = requests.get(urls[0].replace('"', ''), stream=True,headers={'User-agent': 'Mozilla/5.0'})

if r.status_code == 200:
    with open("events/"  + "event" + str(secrets.token_urlsafe(16)) +  ".jpg", 'wb') as f:
        print(f)
        r.raw.decode_content = True
        f.write(r.content)
        shutil.copyfileobj(r.raw, f)
        
    
#urllib.request.urlretrieve(urls[0].replace('"', ''), eventName + ".jpg")
print(os.path.basename("/" + eventName + ".jpg"))


