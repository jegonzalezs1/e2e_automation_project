"""Modulo para importar selenium"""
from selenium.webdriver.common.by import By


def view_cart(driver):
    url = "https://www.demoblaze.com"
    driver.get(url)

    cart = driver.find_element(By.ID, "cat")
    cart = driver.find_element(By.ID, "desc")
    cart = driver.find_element(By.ID, "id")
    cart = driver.find_element(By.ID, "img")
    cart = driver.find_element(By.ID, "price")
    cart = driver.find_element(By.ID, "title")
    cart.click()
