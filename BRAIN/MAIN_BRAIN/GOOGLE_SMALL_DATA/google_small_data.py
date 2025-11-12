import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import traceback


def search_brain(query):
    """
    Print one clean line from Google search result.
    """
    try:
        options = uc.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        driver = uc.Chrome(options=options)
        driver.get("https://www.google.com/")

        # Wait for search bar
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "q")))
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # ✅ Wait until some result elements appear
        WebDriverWait(driver, 10).until(
            lambda d: len(
                d.find_elements(
                    By.CSS_SELECTOR,
                    "div[data-sokoban-container], div.g, div.tF2Cxc, div.VwiC3b, div[role='heading']",
                )
            )
            > 0
        )

        time.sleep(2)  # Let Google load all snippets

        # ✅ Collect visible text from first non-empty result
        elements = driver.find_elements(
            By.CSS_SELECTOR,
            "div[data-sokoban-container], div.tF2Cxc, div.g, div.VwiC3b, div[role='heading']",
        )

        text_content = ""
        for el in elements:
            if el.text.strip():
                text_content = el.text.strip()
                break

        if not text_content:
            print("No search results found.")
            return

        # ✂️ Clean to first readable sentence
        sentences = re.split(r'(?<=[.!?])\s+', text_content)
        filtered = [s for s in sentences if not re.search(r'(https?://|www\.|©|\d{4})', s)]

        result_line = filtered[0] if filtered else sentences[0]

        # ✅ Print single clean line
        print(result_line)

    except Exception as e:
        print("Error occurred:", e)
        traceback.print_exc()

    finally:
        try:
            driver.quit()
        except:
            pass


# ✅ Run example
# search_brain("who is Anubhav Chaturvedi YouTube")
