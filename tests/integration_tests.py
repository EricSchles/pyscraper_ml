from pyscraper_ml import scrapers

def test_requests_scraper():
    try:
        s = scrapers.Scraper(None)
        links = s.run_xpath("https://github.com/EricSchles", "//a/@href")
    except:
        assert False
    assert links != []

def test_chrome_scraper():
    try:
        s = scrapers.Scraper("chrome")
        links = s.run_xpath("https://github.com/EricSchles", "//a/@href")
    except:
        assert False
    assert links != []

def test_firefox_scraper():
    try:
        s = scrapers.Scraper("firefox")
        links = s.run_xpath("https://github.com/EricSchles", "//a/@href")
    except:
        assert False
    assert links != []
