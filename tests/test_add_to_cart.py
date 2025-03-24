"""Modulo para importar selenium"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def add_products_to_cart(driver):
    url = "https://www.demoblaze.com"
    driver.get(url)

    products = ["Samsung galaxy s6", "Apple monitor 24", "Dell i7 8gb"]
    for product_name in products:
        product = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, product_name))
        )
        product.click()
        add_to_cart = driver.find_element(
            By.XPATH, "//a[text()='Add to cart']")
        add_to_cart.click()
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        driver.switch_to.alert.accept()
        driver.back()
