from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import re


def google_answer(query):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    )
    chrome_options.add_argument("--window-size=1920,1080")

    chrome_driver_path = r"C:\Users\PRATI\Desktop\JARVIS4.1\DATA\JARVIS_DRIVER\chromedriver.exe"
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

    driver.get(f"https://www.google.com/search?q={query.replace(' ', '+')}")
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    selectors = [
        ".Z0LcW",                     # Direct Answer Title
        ".e24Kjd",                    # Main direct answer
        ".kno-rdesc span",            # Knowledge panel short desc
        "div[data-attrid='wa:/description']",
        ".VwiC3b"                     # Organic snippet
    ]

    for selector in selectors:
        element = soup.select_one(selector)
        if element and element.get_text(strip=True):
            text = element.get_text(" ", strip=True)
            driver.quit()
            sentences = re.split(r'(?<=[.!?]) +', text)
            return " ".join(sentences[:3])

    driver.quit()
    return "No proper result found."


def deep_answer(query):
    result = google_answer(query)
    print(result)


# deep_answer("What is AI")
# deep_answer("What is Machine learning")
