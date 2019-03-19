# -*- coding: utf-8 -*-

import re
import string
import requests
import urllib.request
import lxml
from bs4 import BeautifulSoup

url = 'https://torrentz2.eu/search'
keywords = {'f':input ("Please input the key words:\n")}

r = requests.get(url,keywords)
print(r.status_code)
# print(r.text)

page = r.text
pagesoup = BeautifulSoup(page,'lxml')
for dl in pagesoup.find_all("dl"):
    dl_str = str(dl)
    dlsoup = BeautifulSoup(dl_str,'lxml')
    a = dlsoup.find_all('a')
    for x in a:
        dd = dlsoup.find_all('span')
        print("The title is "+x.string+"\nThe URL is https://torrentz2.eu"+x["href"]+"\n",end='')
        count = 0
        for span in dd:
            if count == 1:
                print("Time has passed ",end='')
            elif count == 2:
                print("The source size is ",end='')
            elif count == 3:
                print("The rating about it is ",end='')
            elif count == 4:
                print("The peers is ",end='')
            print(span.string,end=' ')
            count = count + 1
        print("\n\n\n")