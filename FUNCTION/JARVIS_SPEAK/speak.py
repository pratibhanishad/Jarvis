from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

# Set up Chrome options to run in the background
chrome_options =uc.ChromeOptions()
chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

driver = webdriver.Chrome(options=chrome_options)
# Specify the path to your Chrome driver executable
# chrome_driver_path = r"C:\Users\PRATI\Desktop\JARVIS4.1\DATA\JARVIS_DRIVER\chromedriver.exe"
#
# # Create a Service object with the specified executable path
# chrome_service = Service(chrome_driver_path)
#
# # Create a Chrome driver instance with the specified options and service
# driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to the website
driver.get("https://tts.5e7en.me/")


def speak(text):
    if not text or not isinstance(text, str):
        print("⚠️ Warning: speak() received invalid text:", text)
        return  # Skip speaking if text is None or empty

    # Wait for the element to be clickable
    element_to_click = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="text"]'))
    )

    element_to_click.click()
    element_to_click.send_keys(text)
    print(text)

    # Calculate sleep duration based on sentence length
    sleep_duration = min(0.2 + len(text) // 5, 5)

    button_to_click = WebDriverWait(driver, 1).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="button"]'))
    )
    button_to_click.click()
    time.sleep(sleep_duration)
    element_to_click.clear()
