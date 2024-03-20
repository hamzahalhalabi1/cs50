import pytest
from project import login_to_instagram
from project import search_on_instagram
from project import construct_search_url


def test_login_to_instagram():
    # Test data
    username = "test_username"
    password = "test_password"
    
    # Perform the test
    login_to_instagram(username, password)
    
    # Check if login is successful by verifying if the current URL is the expected URL after login
    assert driver.current_url == "https://www.instagram.com/"

def test_construct_search_url():
    # Test cases
    hashtag_search = "#test"
    username_search = "@test"
    invalid_search = "test"
    
    # Perform the test
    hashtag_url = construct_search_url(hashtag_search)
    username_url = construct_search_url(username_search)
    invalid_url = construct_search_url(invalid_search)
    
    # Check if URLs are constructed correctly
    assert hashtag_url == "https://www.instagram.com/explore/tags/test/"
    assert username_url == "https://www.instagram.com/test/"
    assert invalid_url is None

def test_search_on_instagram():
    # Test data
    search_driver = webdriver.Chrome(service=service)
    test_search_url = "https://www.instagram.com/explore/tags/test/"
    
    # Perform the test
    search_on_instagram(search_driver, test_search_url)
    
    # Check if the current URL of the driver is the expected search URL
    assert search_driver.current_url == test_search_url
