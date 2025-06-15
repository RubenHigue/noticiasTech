from recolector_rss import recolectar_noticias
from scraper import scrapear_contenido

if __name__ == "__main__":
    noticias = recolectar_noticias()

    for noticia in noticias:
        contenido = scrapear_contenido(noticia["fuente"], noticia["enlace"])
        noticia["contenido_completo"] = contenido
        print(f"\n📝 {noticia['titulo']}\n{contenido[:300]}...\n")
