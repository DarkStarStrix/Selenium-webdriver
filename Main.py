# Selenium WebDriver and game playing bot

import time

from selenium import webdriver

# Set up the webdriver
driver = webdriver.Chrome()
driver.get("https://gabrielecirulli.github.io/2048/")
time.sleep(1)

# Find the game container
game_container = driver.find_element_by_class_name("game-container")


# Find the score container
def get_score():
    return driver.find_element_by_class_name("score-container").text


# Find the retry button
def get_retry_button():
    return driver.find_element_by_class_name("retry-button")


# Find the game over container
def get_game_over():
    return driver.find_element_by_class_name("game-over")


# Find the game won container
def get_game_won():
    return driver.find_element_by_class_name("game-won")
