import requests
from bs4 import BeautifulSoup


def scrape_adslzone(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.content, "html.parser")
    cuerpo = soup.find("div", class_="entry-content") or soup.find("article") or soup
    if not cuerpo:
        return ""
    textos = [p.get_text() for p in cuerpo.find_all("p")]
    return "\n".join(textos[:6])
