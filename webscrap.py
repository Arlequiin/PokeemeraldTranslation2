
import requests
import re
from functions import *
def findmove(move):
    url=f"https://www.google.com/search?q=site%3Apokemondb.net+{move}&source=hp&ei=q5enY5H7H6aM9u8P64q7mAk&iflsig=AJiK0e8AAAAAY6elu6zJo9NjVoJ6KzwNeiyCma4bzkv5&ved=0ahUKEwjR_LOQwJP8AhUmhv0HHWvFDpMQ4dUDCAc&uact=5&oq=site%3Apokemondb.net+{move}&gs_lcp=Cgdnd3Mtd2l6EAM6CwgAEIAEELEDEIMBOggIABCxAxCDAToICC4QsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOgUIABCABDoICAAQgAQQsQM6CwguEIAEELEDEIMBOg4ILhDHARCxAxDRAxCABDoFCAAQsQNQ1QNY6GdgyWtoAXAAeACAAWeIAfQOkgEEMTcuM5gBAKABAaABArABAA&sclient=gws-wiz"
    from bs4 import BeautifulSoup
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    if 'CAPTCHA' in soup.text:
        error(3)
    result=re.findall(f"site:pokepedia.fr {move}(.*?)Pok",soup.text)
    final=re.search(f"{move}(.*) - ",result[0])
    return (final.group(1))
print(findmove('freezngglare'))
