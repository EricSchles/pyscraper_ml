from selenium import webdriver
import concurrent.futures
import requests
import lxml.html
import time
from pyscraper_ml import __version__
import sys

class SimpleScraper:
    def __init__(self, browser):
        self.browser = browser
        if browser == "chrome":
            self.driver = webdriver.Chrome(
                options=self.get_options(),
                executable_path=self.get_executable()
            )
        elif browser == "firefox":
            self.driver = webdriver.Firefox(
                options=self.get_options(),
                executable_path=self.get_executable()
            )

    def get_options(self):
        options = getattr(webdriver, self.browser).options.Options()
        options.headless = True
        return options    

    def run_async(self, func, data, sleep_seconds=0):
        futures = []
        processed_data = []
        with concurrent.futures.ProcessPoolExecutor(max_workers=len(urls)) as pool:
            for datum in data:
                time.sleep(sleep_seconds)
                future = pool.submit(func, datum)
                futures.append(future)
            try:
                for future in concurrent.futures.as_completed(futures):
                    processed_data.append(future.result())
            except concurrent.futures._base.TimeoutError as e:
                print(e.__class__.__name__, e)
            except Exception:
                print(e)
        return processed_data
                
    def get_page(self, url):
        if self.browser:
            self.driver.get(url)
            return self.driver.page_source
        else:
            return requests.get(url).text

    def get_lxml_object(self, url):
        page = self.get_page(url)
        return lxml.html.fromstring(page)

    def get_executable(self):
        if self.browser == "chrome":
            return "/home/eric/Documents/pyscraper_ml/pyscraper_ml/drivers/chromedriver"
        elif self.browser == "firefox":
            return "/home/eric/Documents/pyscraper_ml/pyscraper_ml/drivers/geckodriver"
            # major = sys.version_info.major
            # minor = sys.version_info.minor
            # return f"~/.local/lib/python{major}.{minor}/site-packages/"

    def get_version(self):
        return __version__
    
    def run_xpath(self, url, xpath_str):
        html = self.get_lxml_object(url)
        return html.xpath(xpath_str)

    def run_async_xpath(self, urls, xpath_str):
        htmls = self.run_async(self.get_lxml_object, urls)
        return [
            (urls[i], htmls[i].xpath(xpath_str))
            for i in len(urls)
        ]

