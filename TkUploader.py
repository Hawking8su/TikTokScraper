'''
Upload video to TikTok in Automation
1. using Selenium: pip install undetected_chromedriver
2. Reference: https://github.com/ultrafunkamsterdam/undetected-chromedriver
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import time
import os


def upload_video(video_path):
    try:
        file_input_element = driver.find_elements(By.XPATH, r'//*[@id="root"]/div/div/div/div/div[2]/div[1]/div/input')[0]
        print("element text: {} | id: {}".format(file_input_element.text, file_input_element.id))
    except Exception as e:
        print("Error: {}".format(e))
    abs_video_path = os.path.join(os.getcwd(), video_path)
    print()
    if not os.path.exists(abs_video_path):
        raise FileNotFoundError(abs_video_path)
    file_input_element.send_keys(video_path)
    driver.implicitly_wait(5) # wait for upload

# note: default caption text = video file name
def set_caption_tag(tags_str):
    tags_list = tags_str.split("#")
    if len(tags_list) <=0: return None
    try:
        caption_input_element = driver.find_element(By.XPATH,
                                                    r'//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div/div')
        for tag_name in tags_list:
            if tag_name == '' : continue
            caption_input_element.send_keys("#{}".format(tag_name))
            time.sleep(2)
            caption_input_element.send_keys(Keys.RETURN)
            time.sleep(1)
    except Exception as e:
        print("Error: {}".format(e))

# post button
# //*[@id="root"]/div/div/div/div/div[2]/div[2]/div[7]/div[2]
def click_post():
    try:
        post_button_element = driver.find_element(By.XPATH, value= r'//*[@id="root"]/div/div/div/div/div[2]/div[2]/div[7]/div[2]')
        print("element text: {} | id: {}".format(post_button_element.text, post_button_element.id))
        post_button_element.click()
    except Exception as e:
        print("Error: {}".format(e))

if __name__ == "__main__":
    # keep user data for auto-login
    options = uc.ChromeOptions()
    options.user_data_dir = "selenium"
    driver = uc.Chrome(options=options)
    # login manually
    time.sleep(5)
    driver.get('https://www.tiktok.com/login/?lang=en')
    time.sleep(5)

    driver.get('https://www.tiktok.com/upload/?lang=en')
    # switch to iframe
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    # elems = driver.find_elements(by = By.TAG_NAME, value = 'iframe')
    driver.switch_to.frame(0)
    driver.implicitly_wait(1)

    video_path = "video/cat eating meal.mp4"
    upload_video(os.path.abspath(video_path))
    time.sleep(5)
    tags_str = "cat eating meal #cat"
    set_caption_tag(tags_str)
    driver.implicitly_wait(3)
    # click_post()
    time.sleep(3)
