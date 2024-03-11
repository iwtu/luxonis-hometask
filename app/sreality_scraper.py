from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from typing import List

from model import FlatModel


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


def _get_html_page(page):
    url = f"https://www.sreality.cz/hledani/prodej/byty?strana={page}"
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=options
    )

    driver.get(url)

    timeout = 5
    element_class_name = "dir-property-list"
    try:
        element_present = EC.presence_of_element_located(
            (By.CLASS_NAME, element_class_name)
        )
        WebDriverWait(driver, timeout).until(element_present)
    except TimeoutException:
        print(
            f"Website {url} doesn't contain class element {element_present} after loading for {timeout} seconds"
        )
        return None

    return driver.page_source


def scrape_flats(flat_count=500) -> List[FlatModel]:
    flats = []
    page = 1
    while True:
        html = _get_html_page(page)
        # with open("sreality.html", "w") as text_file:
        #     text_file.write(html)
        soup = BeautifulSoup(html, "html.parser")
        flat_items = soup.find_all(class_="property")
        print(f"FLATS : {len(flat_items)}")
        for flat in flat_items:
            if len(flats) >=  flat_count:
                return flats

            title = flat.find(class_="name").get_text()
            img_url = flat.find_all("img")[0]["src"]

            print(f"Title: {title}, img: {img_url}")
            flats.append(FlatModel(title, img_url))

        page = page + 1

    # return flats
