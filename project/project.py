import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from urllib.parse import urlparse
import requests

# Function to create directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to download image from URL
def download_image(url, directory):
    response = requests.get(url)
    if response.status_code == 200:
        with open(directory, 'wb') as file:
            file.write(response.content)

# Function to extract image URLs from Instagram page
def extract_image_urls(driver, url):
    driver.get(url)
    time.sleep(5)  # Wait for the page to load

    img_urls = set()
    # Scroll down the page to load more images
    for _ in range(5):  # Adjust the range as needed
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3) 

    # Find all image elements
    img_elements = driver.find_elements(By.TAG_NAME, 'img')
    for img_element in img_elements:
        img_url = img_element.get_attribute('src')
        if img_url and 'https' in img_url:
            img_urls.add(img_url)

    return img_urls

# Function to login to Instagram
def login_to_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)  # Wait for the page to load

    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    time.sleep(5)  # Wait for the login process

# Main function
def main():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed
    driver.maximize_window()

    # Your Instagram credentials
    username = 'hamzah.alhalabi'
    password = 'Bruhmoment1@'

    # Login to Instagram
    login_to_instagram(driver, username, password)

    # URL of the Instagram page to scrape
    url = "https://www.instagram.com/sobkays/"

    # Extract image URLs
    image_urls = extract_image_urls(driver, url)

    # Directory to save images
    download_dir = "instagram_images"
    create_directory(download_dir)

    # Download images
    for idx, img_url in enumerate(image_urls):
        image_name = f"image_{idx}.jpg"  # You can change the naming convention if needed
        download_path = os.path.join(download_dir, image_name)
        download_image(img_url, download_path)
        print(f"Downloaded {image_name}")

    # Close the WebDriver
    driver.quit()

if __name__ == "__main__":
    main()
