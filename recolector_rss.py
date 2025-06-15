import feedparser

# Lista de fuentes RSS tecnológicas
feeds = {
    "BBC": "https://feeds.bbci.co.uk/news/technology/rss.xml",
    "TechCrunch": "https://techcrunch.com/feed/",
    "The Verge": "https://www.theverge.com/rss/index.xml",
    "Wired": "https://www.wired.com/feed/rss",
    "New York Times": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
    "Reuters": "https://rss.app/feeds/oeTaZ4HohO2RPhEf.xml",
    "CNN": "https://rss.app/feeds/1jIzW5ADwWTnkBHC.xml",
    "El economista": "https://rss.app/feeds/JEvOcsfOfrv4pV3K.xml",
    "La vanguardia": "https://www.lavanguardia.com/rss/tecnologia.xml",
    "ADSL zone": "https://rss.app/feeds/T1FKchiVuoLyQREZ.xml"
}

# Número de noticias por fuente
NOTICIAS_POR_FUENTE = 5


# Función para recolectar noticias
def recolectar_noticias():
    noticias = []

    for nombre, url in feeds.items():
        feed = feedparser.parse(url)
        print(f"\n📰 Fuente: {nombre}")

        for entry in feed.entries[:NOTICIAS_POR_FUENTE]:
            noticia = {
                "titulo": entry.title,
                "enlace": entry.link,
                "resumen": entry.get("summary", ""),
                "fuente": nombre
            }
            noticias.append(noticia)

            print(f" - {noticia['titulo']}")

    return noticias