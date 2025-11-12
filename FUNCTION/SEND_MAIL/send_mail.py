from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
from selenium.webdriver.support.wait import WebDriverWait


def search_and_extract(text):
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")


        chrome_driver_path=r'C:\Users\PRATI\Desktop\JARVIS4.1\DATA\JARVIS_DRIVER\chromedriver.exe'
        chrome_service= Service(chrome_driver_path)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.get("https://www.google.com")
        search_box = driver.find_element( "name", "q")


        search_query = text
        search_box.send_keys(search_query)

        search_box.send_keys(Keys.RETURN)
        # Wait for the search box to be present (adjust the timeout as needed)
        WebDriverWait(driver,  10).until(EC.presence_of_element_located((By.NAME)))

       # Find the first search result element
        first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')

        # Extract the link of the first result
        first_result_link = first_result.find_element(By.CSS_SELECTOR, 'a').g

        # Visit the first result link
        driver.get(first_result_link)

        webpage_content = driver.page_source

        # Parse the webpage content with BeautifulSoup
        soup = BeautifulSoup(webpage_content, 'html.parser')

        # Extract text from the webpage, excluding script and style tags
        webpage_text = ''.join([p.get_text() for p in soup.find_all('p')])

        # Extract keywords or relevant information based on your specific requireme
        # For example, you can use a keyword extraction library or manually define

        # Extract and print the first 8-9 sentences from the webpage text
        sentences = re.split('(?<=[.!?])\s', webpage_text)
        result_text = ''.join(sentences[:9])
        return result_text

    except Exception as e:
        print("An error occurred:", e)

    except Exception as e:
        print("An error occurred:", e)

    driver.quit()

################################################################
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


# usage
def summarize_text(text, sentences_count=5):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count)
    return ''.join([str(sentence) for sentence in summary])


# Example usage
# usage
def summary(text):
    text_to_summarize = text
    summary_result = summarize_text(text_to_summarize)
    print(summary_result)


# usages
def deep_search(text):
    x = text
    y=search_and_extract(x)
    summary(y)

deep_search("what is machine learning")
deep_search("what is AI")