from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


def collectStuff():
    options = Options()
    options.add_argument("--disable-infobars")
    #options.add_argument("headless")
    options.add_experimental_option("prefs", {
        "profile.default_content_setting_values.notifications": 1
    })
    driver = webdriver.Chrome(executable_path='/Users/jakewriter/downloads/chromedriver 2', options=options)
    driver.get('https://agar.io/')
    agarWindow = driver.current_window_handle
    time.sleep(8)
    signInButton = driver.find_element_by_id('googleLogin')
    signInButton.click()
    time.sleep(2)
    for handle in driver.window_handles:
        if handle is not agarWindow:
            driver.switch_to.window(handle)

    username = driver.find_element_by_id("identifierId")
    username.click()
    username.send_keys("xjawbone04x@gmail.com")
    nextButton = driver.find_element_by_id('identifierNext')
    nextButton.click()

    time.sleep(2)
    password = driver.find_element_by_class_name("whsOnd")
    password.click()
    password.send_keys("cheeppeep11")
    passbutton = driver.find_element_by_id('passwordNext')
    passbutton.click()
    driver.switch_to.window(agarWindow)
    time.sleep(7)

    coinButton = driver.find_element_by_id("freeCoins")
    coinButton.click()
    time.sleep(1)
    from pynput.mouse import Button, Controller
    mouse = Controller()
    button = Button.left
    mouse.position = (888, 355)
    mouse.click(button)
    time.sleep(2)
    labels = driver.find_elements_by_xpath("//span[@class='label']")
    for label in labels:
        if label.text == 'Start':
            label.click()
        if label.text == 'Open':
            label.click()
            skipButton = driver.find_element_by_id('')
            skipButton.click()
            closeButton = driver.find_element_by_id('')
            closeButton.click()
    driver.close()


while True:
    collectStuff()
    time.sleep(3607)