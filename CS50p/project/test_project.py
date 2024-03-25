import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import stdiomask
import requests
from unittest.mock import patch

from project import login_to_instagram
from project import search_on_instagram
from project import construct_search_url
from project import save_images

# Mocking user input for testing purposes
@patch('builtins.input')
def test_login_and_search(mock_input):
    mock_input.side_effect = ['username', 'password', '@test_user']

    driver = webdriver.Chrome()
    login_to_instagram(driver, 'username', 'password')
    assert driver.current_url == 'https://www.instagram.com/'

    search_url = construct_search_url('@test_user')
    search_on_instagram(driver, search_url)
    assert driver.current_url == f'https://www.instagram.com/test_user/'

    driver.quit()

def test_construct_search_url():
    assert construct_search_url('@test_user') == 'https://www.instagram.com/test_user/'
    assert construct_search_url('#test_tag') == 'https://www.instagram.com/explore/tags/test_tag/'

def test_save_images(tmpdir):
    driver = webdriver.Chrome()
    driver.get('https://www.instagram.com/test_user/')
    dest_loc = tmpdir.mkdir('images')
    save_images(driver, dest_loc)
    assert len(os.listdir(dest_loc)) > 0
    driver.quit()
