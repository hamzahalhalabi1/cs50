import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import stdiomask
import requests
import os

def get_user_input():
    my_user = input("Phone number, username, or email: ")
    my_password = stdiomask.getpass(prompt='Enter your password: ', mask='*')
    search_for = input("@ or #: ")
    return my_user, my_password, search_for

def login_to_instagram(driver, username, password):
    driver.get("https://www.instagram.com/")
    driver.maximize_window()
    user_name = driver.find_element(By.XPATH, "//input[@name='username']")
    user_name.send_keys(username)
    user_name.send_keys(Keys.ENTER)
   
    password_field = driver.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)
    sleep(5)
    # Ignore Popups
    save_info = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[role="button"]')))
    save_info.click()
    notification = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button._a9--._ap36._a9_1')))
    notification.click()

def search_on_instagram(driver, search_url):
    if search_url:
        driver.get(search_url)

def construct_search_url(search_for):
    if "#" in search_for:
        return f"https://www.instagram.com/explore/tags/{search_for.replace('#', '')}/"
    elif "@" in search_for:
        return f"https://www.instagram.com/{search_for.replace('@', '')}/"
    else:
        print("Invalid search input. Please provide a valid search term.")
        return None

def save_images(driver, dest_loc):
    # Scroll down the webpage
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for some time to let the page load completely after scrolling
    sleep(5)

    # Save images
    image_elements = driver.find_elements(By.XPATH, '//img[@class="x5yr21d xu96u03 x10l6tqk x13vifvy x87ps6o xh8yej3"]')
    # Iterate over image elements and save them to the destination folder
    for index, image_element in enumerate(image_elements):
        image_source = image_element.get_attribute('src')
        print("Downloading Image:", image_source)
        # Download the image using requests
        response = requests.get(image_source)
        if response.status_code == 200:
            # Construct the filename for the image
            filename = f"image_{index}.jpg"  # You can modify the filename as per your requirement
            filepath = os.path.join(dest_loc, filename)
            # Save the image to the destination folder
            with open(filepath, 'wb') as f:
                f.write(response.content)
            print("Image saved as:", filepath)
        else:
            print("Failed to download image:", image_source)

def main():
    dest_loc = r'C:\Users\hamza\PycharmProjects\CS50P\CS50p\project\images'
    PATH = "C:\Program Files\drivers\chromedriver.exe"  # Driver path
    service = Service(PATH)
    driver = webdriver.Chrome(service=service)

    my_user, my_password, search_for = get_user_input()
    login_to_instagram(driver, my_user, my_password)
    search_url = construct_search_url(search_for)
    search_on_instagram(driver, search_url)
    save_images(driver, dest_loc)

if __name__ == "__main__":
    main()
