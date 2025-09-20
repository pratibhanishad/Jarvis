from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import undetected_chromedriver as uc
import traceback
import re

# ✅ Fix WinError destructor issue
uc.Chrome.__del__ = lambda self: None

# Setup driver
chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--headless")   # 👉 Uncomment if you want background mode
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=chrome_options, version_main=139)


def realtimeDataBrain(query):
    try:
        print(f"\nSearch Query: {query}\n")
        driver.get("https://www.google.com")
        # Accept cookies (if popup appears)
        try:
            agree_btn = WebDriverWait(driver, 3).until(
                EC.element_to_be_clickable((By.XPATH, "//button//*[text()='I agree']"))
            )
            agree_btn.click()
        except:
            pass

        # Enter query
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results
        first_results = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//h3/ancestor::a"))
        )

        # Default first link
        first_result_link = first_results[0].get_attribute("href")

        # Prefer Wikipedia if available
        wiki_link = None
        for r in first_results:
            href = r.get_attribute("href")
            if "wikipedia.org" in href:
                wiki_link = href
                break

        link_to_open = wiki_link if wiki_link else first_result_link
        print(f"Top Link: {link_to_open}\n")

        driver.get(link_to_open)

        # Get webpage content
        webpage_content = driver.page_source
        soup = BeautifulSoup(webpage_content, 'html.parser')

        # Extract <p> text
        webpage_text = ' '.join([p.get_text() for p in soup.find_all('p')])

        # Pick first sentences
        sentences = re.split(r'(?<=[.!?])\s', webpage_text)
        result_text = '. '.join(sentences[:6])  # first 6 sentences only


        return result_text

    except Exception as e:
        print("Error:", e)
        traceback.print_exc()

    finally:
        driver.quit()
