import re
import requests
from bs4 import BeautifulSoup

respons=requests.get('https://www.imdb.com/')

soup=BeautifulSoup(respons.text,'html.parser')

movie=str(soup.find_all('span'))

matn=re.findall(r'span class="SlideCaption__WithPeekCaptionHeadingText-u5mma4-4 cfvKkH">(.*?)?<',movie)
print("\n")
for i in range(0,len(matn)):
    print(matn[i],"\n","-------------------","\n")


