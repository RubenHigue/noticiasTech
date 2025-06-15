import requests
from bs4 import BeautifulSoup

def scrape_bbc(url):
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(r.content, "html.parser")

    # BBC suele poner el contenido en <article> o divs con role="main"
    cuerpo = soup.find("article") or soup.find("main") or soup
    if not cuerpo:
        return ""

    textos = [p.get_text() for p in cuerpo.find_all("p")]
    return "\n".join(textos[:6])  # Limita a 6 párrafos por ejemplo
