import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from FUNCTION.JARVIS_SPEAK.speak import speak


def get_internet_speed():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode (without opening a browser window)

    # Set the path to your ChromeDriver executable
        chrome_driver_path = r'C:\Users\PRATI\Desktop\JARVIS4.1\DATA\JARVIS_DRIVER\chromedriver.exe'

        service = ChromeService(chrome_driver_path)
        driver = webdriver.Chrome(service=service)


        # Open the website
        driver.get('https://fast.com')
        speak("checking your internet speed")
        time.sleep(11)# Replace with the actual website URL

        # Find the element with the speed value
        speed_element = driver.find_element(By.ID,'speed-value')

        # Get the text value from the element
        speed_value = speed_element.text

        return speed_value
    except Exception as e:
        print(f"Error:{e}")
        return None
    finally:
        if driver:
         driver.quit()


def check_internet_speed():
    speed_result = get_internet_speed()

    if speed_result is not None:
        speak(f"Sir, your internet speed is: {speed_result} Mbps")
    else:
        speak("Error: Unable to retrieve internet speed.")
