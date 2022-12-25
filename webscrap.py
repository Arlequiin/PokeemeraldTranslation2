
import requests
import re

def findmove(move):
    url=f"https://www.google.com/search?q=site%3Apokepedia.fr+{move}&client=opera&hs=4rc&ei=oI2nY8ymHuLgsAfzj4KABw&ved=0ahUKEwjM9rjGtpP8AhViMOwKHfOHAHAQ4dUDCA4&uact=5&oq=site%3Apokepedia.fr+{move}&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAUoECEYYAFDsBliUGGC4GmgBcAB4AIABZIgB0QmSAQQxMi4xmAEAoAEBwAEB&sclient=gws-wiz-serp"
    from bs4 import BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    result=re.findall(f"site:pokepedia.fr {move}(.*?)Pok",soup.text)
    final=re.search(f"{move}(.*) - ",result[0])
    return (final.group(1))
print(findmove('freezngglare'))
