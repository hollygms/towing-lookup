import time
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from filter_data import filter_vins
from selenium import webdriver
from selenium.webdriver.common.by import By
import platform
from config import FORD_URL


vins_to_search = filter_vins()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(FORD_URL)

def get_ford_towing():
    """Automates the chrome browser to open the Ford Url, search the VIN's in vins_to_search,
    then scrapes the Max Towing Capacity from the site.
    Returns a dictionary of VIN: Max Towing Capacity"""
    ford_vin_towing = {}

    for vin in vins_to_search:

        #pop up that needs to be clicked to dismiss if it's displayed
        verify = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div[1]/div[3]/div/div[2]/div/button')
        if verify.is_displayed():
            verify.click()

        search = driver.find_element(By.XPATH, '//*[@id="VIN-label"]')
        # clear() isnt working so need to clear based on operating system
        #if clear() ever works, use that instead of the if statement
        if platform.system() == 'Windows':
            search.send_keys(Keys.CONTROL, 'a', Keys.DELETE)
        else:
            search.send_keys(Keys.COMMAND, 'a', Keys.DELETE)

        search.send_keys(vin)

        button = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div[1]/section/div/section/div[2]/div[4]/button')
        button.click()
        time.sleep(2)

        #searching for the towing capacity and cleaning the string
        try:
            value = driver.find_element(By.XPATH, '//*[@id="cittHitchTypeTabspanel0"]/section/div[3]/span[2]').text
            value = value.split()[0]
            next_vehicle = driver.find_element(By.XPATH, '//*[@id="root"]/div/main/div[1]/section/div/div[2]/div[3]/button')
            next_vehicle.click()

        except NoSuchElementException:
            value = 'VIN ERROR'

        finally:
            ford_vin_towing[vin] = value

    driver.quit()
    return ford_vin_towing

