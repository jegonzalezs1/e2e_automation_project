"""Modulo para importar"""

import json
from selenium.webdriver.common.by import By


def complete_purchase(driver):
    url = "https://www.demoblaze.com"
    driver.get(url)

    path = "resources/data.json"
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
        place_order = driver.find_element(
            By.XPATH, "//button[text()='Place Order']")
        place_order.click()

        driver.find_element(By.ID, "cat").send_keys(data["cat"])
        driver.find_element(By.ID, "desc").send_keys(data["desc"])
        driver.find_element(By.ID, "id").send_keys(data["id"])
        driver.find_element(By.ID, "img").send_keys(data["img"])
        driver.find_element(By.ID, "price").send_keys(data["price"])
        driver.find_element(By.ID, "title").send_keys(data["title"])

        purchase = driver.find_element(By.XPATH, "//button[text()='Purchase']")
        purchase.click()
