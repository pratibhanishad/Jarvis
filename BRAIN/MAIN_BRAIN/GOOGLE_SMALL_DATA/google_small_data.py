from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = None  # Global driver

def get_driver():
    """Start Chrome driver (fresh instance)."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # background mode
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--window-size=1920,1080")

    chrome_driver_path = r"C:\Users\PRATI\Desktop\JARVIS4.1\DATA\JARVIS_DRIVER\chromedriver.exe"
    chrome_service = Service(chrome_driver_path)
    return webdriver.Chrome(service=chrome_service, options=chrome_options)


def search_brain(query):
    """Search Google for query and return clean result."""
    global driver
    if driver is None:
        driver = get_driver()

    try:
        driver.get("https://www.google.com")

        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # ✅ Try Knowledge Panel (right side box)
        try:
            kp_title = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-attrid='title'] span"))
            ).text

            kp_desc = driver.find_element(By.CSS_SELECTOR, "div[data-attrid='description'] span").text

            return {"title": f"{kp_title}\n{kp_desc}", "url": driver.current_url}
        except:
            pass

        # ✅ If no knowledge panel → take first search result
        first_result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "(//h3)[1]"))
        )
        parent = (
            first_result.find_element(By.XPATH, "./ancestor::a")
            if first_result.tag_name != "a"
            else first_result
        )

        title = parent.text
        url = parent.get_attribute("href")

        # Clean text
        sentences = re.split(r'(?<=[.!?])\s', title)
        filtered_sentences = [s for s in sentences if not re.search(r'https?://\S+', s)]
        result_text = '. '.join(filtered_sentences[:5])
        result_text = result_text.replace("Featured snippet from the web,", "")

        return {"title": result_text, "url": url}

    except Exception as e:
        print(f"⚠️ Error while searching '{query}': {e}")
        try:
            if driver:
                driver.quit()
        except:
            pass
        driver = None
        return None


def run_queries(queries):
    if isinstance(queries, str):
        queries = [queries]

    for q in queries:
        result = search_brain(q)
        if result:
            print(f"\n🔹 Query: {q}\n")
            print(result["title"])  # 👈 Clean format like screenshot
            print(result["url"])

        else:
            print(f"\n No result for query: {q}")

