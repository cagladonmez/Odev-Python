from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest


class test_Odev8:
    
    def setup_method(self):

        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
    
    def teardown_method(self):
        self.driver.quit()

    def test_taxDelivery(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("standard_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        item1 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        item1.click()
        item2 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        item2.click()
        shoppingCart = self.driver.find_element(By.LINK_TEXT, "2")
        shoppingCart.click()
        checkOutButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
        checkOutButton.click()
        firstName = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]")
        firstName.send_keys("Çağla")
        lastName = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]")
        lastName.send_keys("Dönmez")
        postalCode = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]")
        postalCode.send_keys("12345")
        ContinueButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]")
        ContinueButton.click()
        DeliveryMessage = self.driver.find_element(By.CSS_SELECTOR, ".summary_value_label:nth-child(4)")
        assert DeliveryMessage.text ==  "Free Pony Express Delivery!"
        taxMessage = self.driver.find_element(By.CSS_SELECTOR, ".summary_tax_label")
        assert taxMessage.text ==  "Tax: $3.20"


    def test_successfulOrder(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("standard_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]")))
        Item1 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        Item1.click()
        Item2 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]")
        Item2.click()
        Item3 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-fleece-jacket\"]")
        Item3.click()
        Item4 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-onesie\"]")
        Item4.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "4")))
        shoppingCart = self.driver.find_element(By.LINK_TEXT, "4")
        shoppingCart.click()
        checkoutButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
        checkoutButton.click()
        firstName = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]")
        firstName.send_keys("Çağla")
        lastName = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]")
        lastName.send_keys("Dönmez")
        postalCode = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]")
        postalCode.send_keys("12345")
        ContinueButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]")
        ContinueButton.click()
        FinishButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"finish\"]")
        FinishButton.click()
        Message = self.driver.find_element(By.CSS_SELECTOR, ".complete-header")
        assert Message.text == "Thank you for your order!"


    def test_problemOrder(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("problem_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]")))
        Item1 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        Item1.click()
        Item2 = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"add-to-cart-sauce-labs-bike-light\"]")
        Item2.click()
        shoppingCart = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_badge")
        shoppingCart.click()
        checkOutButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
        checkOutButton.click()
        ContinueButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]")
        ContinueButton.click()
        errorMessage = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]")
        assert errorMessage.text == "Error: First Name is required"

    def test_postalCode(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("standard_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        shoppingCart = self.driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link")
        shoppingCart.click()
        checkOutButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"checkout\"]")
        checkOutButton.click()
        firstName = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"firstName\"]")
        firstName.send_keys("Çağla")
        lastName = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"lastName\"]")
        lastName.send_keys("Dönmez")
        postalCode = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"postalCode\"]")
        postalCode.send_keys("12345")
        ContinueButton = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"continue\"]")
        ContinueButton.click()
        errorMessage = self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"error\"]")
        assert errorMessage.text == "Error: Postal Code is required"


       


    def test_itemNotFound(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("problem_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        Item = self.driver.find_element(By.CSS_SELECTOR, "#item_5_img_link > .inventory_item_img")
        Item.click()
        Message = self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_desc")
        assert Message.text == "We\\\'re sorry, but your call could not be completed as dialled. Please check your number, and try your call again. If you are in need of assistance, please dial 0 to be connected with an operator. This is a recording. 4 T 1."
        MessageHead = self.driver.find_element(By.CSS_SELECTOR, ".inventory_details_name")
        assert MessageHead.text == "ITEM NOT FOUND"
