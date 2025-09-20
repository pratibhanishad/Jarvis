import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)


driver = webdriver.Chrome(options=chrome_options)


driver.get("https://tts.5e7en.me/")

def speak(text):
    try:
        # Wait for the element to be clickable
        element_to_click = WebDriverWait(driver, timeout=2).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
        )

        # Perform the click action
        element_to_click.click()

        # Input text into the element
        element_to_click.send_keys(text)
        print(text)

        # Calculate sleep duration based on sentence length
        sleep_duration = min(1 + len(text) // 30,10)

        # Wait for the button to be clickable
        button_to_click = WebDriverWait(driver, timeout=5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
        )

        # Perform the click action on the button
        button_to_click.click()

        # Sleep for dynamically calculated duration
        time.sleep(sleep_duration)

        # Clear the text box for the next sentence
        element_to_click.clear()

    except Exception as e:
        print(f"[ERROR] in speak(): {e}")
