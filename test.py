from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import re
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def search_and_extract(text):
    driver = None
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        chrome_driver_path = r'C:\Users\PRATI\Desktop\JARVIS4.1\DATA\JARVIS_DRIVER\chromedriver.exe'
        driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
        driver.get("https://www.google.com")

        # Search on Google
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(text)
        search_box.send_keys(Keys.RETURN)

        # Wait for first search result
        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//a/h3)[1]/ancestor::a"))
        )
        first_link = first_result.get_attribute("href")

        # Open the first result
        driver.get(first_link)
        WebDriverWait(driver, 5).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        # Parse the content
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Extract meaningful content (not only <p>)
        texts = []

        for tag in ["p", "article", "section", "div"]:
            for element in soup.find_all(tag):
                content = element.get_text(" ", strip=True)
                if len(content.split()) > 20:  # filter small junk
                    texts.append(content)

        # Join all texts
        webpage_text = " ".join(texts).strip()

        if not webpage_text or len(webpage_text) < 200:
            return None  # insufficient content

        # Keep only first 15 sentences to avoid too-long input
        sentences = re.split(r'(?<=[.!?])\s+', webpage_text)
        return " ".join(sentences[:15])

    except Exception:
        return None

    finally:
        if driver:
            driver.quit()


def summarize_text(text, sentences_count=5):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences_count)
        return ' '.join(str(sentence) for sentence in summary)
    except Exception:
        return text[:500]  # fallback partial text


def deep_search(query):
    extracted_text = search_and_extract(query)
    if extracted_text:
        summarized = summarize_text(extracted_text)
        print(summarized)
    else:
        print("Sorry, no readable content found on the first result.")


