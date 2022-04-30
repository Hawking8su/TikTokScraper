'''
Upload video to TikTok
Background:
1. TikTok official API doesn't support video upload, so use selenium
Reference:
1. https://github.com/redianmarku/tiktok-autouploader/blob/main/run.py
2. https://github.com/makiisthenes/TiktokAutoUploader

TODO:
1. Problem: cannot find the right element
'''
import time
from selenium import webdriver


print('=====================================================================================================')
print('Hey, you have to login manully on tiktok, so the bot will wait you 1 minute for loging in manually!')
print('=====================================================================================================')
# time.sleep(8)
print('Running bot now, get ready and login manually...')
time.sleep(4)

options = webdriver.ChromeOptions()

## Hide automation status
# For older ChromeDriver under version 79.0.3945.1600
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)

# For ChromeDriver version 79.0.3945.16 or over
options.add_argument('--disable-blink-features=AutomationControlled')

## Hold cookies to avoid login
options.add_argument("--user-data-dir=selenium")


# Provide the path of chromedriver present on your system.
driver = webdriver.Chrome(executable_path="chromedriver",
                          chrome_options=options)
driver.set_window_size(1080, 600)

# Send a get request to the url
driver.get('https://www.tiktok.com/login')
time.sleep(20)
# login manually
driver.get('https://www.tiktok.com/upload/?lang=en')
time.sleep(5)

# Find upload button
xpath = '/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div/div[4]/button/div/div'
elements = driver.find_elements_by_xpath(xpath)  ## empty list, cannot find the right element

## todo:
## step1: auto login

## step2: find the right upload button

## step3: finish upload process

driver.quit()
print("Done")