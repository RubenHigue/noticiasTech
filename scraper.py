from scrapers import bbc, adsl_zone  # Importa más según los vayas creando

router = {
    "BBC": bbc.scrape_bbc,
    "ADSL zone": adsl_zone.scrape_adslzone
}


def scrapear_contenido(fuente, url):
    funcion_scraper = router.get(fuente)
    if funcion_scraper:
        try:
            return funcion_scraper(url)
        except Exception as e:
            print(f"❌ Error en scraper de {fuente}: {e}")
    else:
        print(f"⚠️ No hay scraper definido para {fuente}")
    return ""
