from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_saucedemo:

    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com")
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok = True)

    def teardown_method(self):
        self.driver.quit()

    def test_NoUsername(self):
       loginbutton = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")
       loginbutton.click()
       errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
       self.driver.save_screenshot(f"{self.folderPath}/NoUsername.png")
       assert errorMessage.text =="Epic sadface: Username is required"

    def test_NoPassword(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        UsernameInput.send_keys("standard_user")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/NoPassword.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    def test_LockedOutUser(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        UsernameInput.send_keys("locked_out_user")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/LockedOutUser.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_standardUser(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("standard_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        url = self.driver.current_url
        assert url == "https://www.saucedemo.com/inventory.html"
        InventoryList = self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        print(f"Bu sitede {len(InventoryList)} adet ürün var")
        self.driver.save_screenshot(f"{self.folderPath}/Inventory.png")
        assert len(InventoryList) == 6
        
    def test_XIcon(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"login-button")))
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        XIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        self.driver.save_screenshot(f"{self.folderPath}/errorIconExists.png")
        assert len(XIcons)!=0
        Xbutton = self.driver.find_element(By.CLASS_NAME,"error-button")
        Xbutton.click()
        XIcons = self.driver.find_elements(By.CLASS_NAME,"error_icon")
        self.driver.save_screenshot(f"{self.folderPath}/NoIcon.png")
        assert len(XIcons)==0

    def test_problemUser(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("problem_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"add-to-cart-sauce-labs-backpack")))
        AddButton = self.driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        AddButton.click()
        ShoppingCart = self.driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        ShoppingCart.click()
        price = self.driver.find_element(By.CLASS_NAME,"inventory_item_price")
        self.driver.save_screenshot(f"{self.folderPath}/shoppingcart.png")
        assert price.text == "$29.99"

    def test_PerformanceGlitchUser(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys("performance_glitch_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        Item = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[5]/div[2]/div[1]/a/div")
        self.driver.save_screenshot(f"{self.folderPath}/perfGlitchUser.png")
        assert Item.text == "Sauce Labs Onesie"

    @pytest.mark.parametrize("username,password",[("çağla","çokgizlişifre"),("kreyziboy32","12345"),("cr@zy8oi","hotgirl23")])
    def test_InvalidLogin(self,username,password):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"user-name")))
        UsernameInput = self.driver.find_element(By.ID,"user-name")
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        PasswordInput = self.driver.find_element(By.ID,"password")
        UsernameInput.send_keys(username)
        PasswordInput.send_keys(password)
        loginbutton = self.driver.find_element(By.ID,"login-button")
        loginbutton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]")
        self.driver.save_screenshot(f"{self.folderPath}/InvalidLogin-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"