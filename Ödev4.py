from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Testsaucedemo:

    def NoUsername(self):
       driver = webdriver.Chrome(ChromeDriverManager().install())
       sleep(2)
       driver.maximize_window()
       sleep(2)
       driver.get("https://www.saucedemo.com/")
       loginbutton = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/input")
       sleep(2)
       loginbutton.click()
       sleep(2)
       errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
       sleep(2)
       testResult = errorMessage.text =="Epic sadface: Username is required"
       print(f"Test Sonucu: {testResult}")
       sleep(5)

    def NoPassword(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        sleep(2)
        driver.maximize_window()
        sleep(2)
        driver.get("https://www.saucedemo.com/")
        UsernameInput = driver.find_element(By.ID,"user-name")
        UsernameInput.send_keys("standard_user")
        loginbutton = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginbutton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Test Sonucu: {testResult}")
        sleep(5)

    def LockedOutUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        sleep(2)
        driver.maximize_window()
        sleep(2)
        driver.get("https://www.saucedemo.com/")
        UsernameInput = driver.find_element(By.ID,"user-name")
        UsernameInput.send_keys("locked_out_user")
        PasswordInput = driver.find_element(By.ID,"password")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginbutton.click()
        sleep(2)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Test Sonucu: {testResult}")
        sleep(5)

    def standardUser(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        driver.maximize_window()
        sleep(2)
        driver.get("https://www.saucedemo.com/")
        UsernameInput = driver.find_element(By.ID,"user-name")
        PasswordInput = driver.find_element(By.ID,"password")
        sleep(2)
        UsernameInput.send_keys("standard_user")
        PasswordInput.send_keys("secret_sauce")
        loginbutton = driver.find_element(By.ID,"login-button")
        sleep(2)
        loginbutton.click()
        sleep(2)
        url = driver.current_url
        testResult = url == "https://www.saucedemo.com/inventory.html"
        if testResult == False:
            print(f"Test Sonucu: {testResult}")
            sleep(5)
        else:
            InventoryList = driver.find_elements(By.CLASS_NAME,"inventory_item")
            sleep(2)
            print(f"Bu sitede {len(InventoryList)} adet ürün var")
            testResult = len(InventoryList) == 6
            print(f"Test Sonucu: {testResult}")
            sleep(5)

    def XIcon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        sleep(2)
        driver.maximize_window()
        sleep(2)
        driver.get("https://www.saucedemo.com/")
        loginbutton = driver.find_element(By.ID,"login-button")
        loginbutton.click()
        sleep(2)
        XIcons = driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg")
        sleep(2)
        testResult = len(XIcons)!=0
        if testResult == False:
            print(f"Test Sonucu: {testResult}")
        else:
            Xbutton = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button/svg/path")
            sleep(2)
            Xbutton.click()
            sleep(2)
            XIcons = driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/svg")
            testResult = len(XIcons)==0
            print(f"Test Sonucu: {testResult}")
        while True:
            continue

Testsaucedemo().NoPassword()
Testsaucedemo().NoUsername()
Testsaucedemo().LockedOutUser()
Testsaucedemo().standardUser()
Testsaucedemo().XIcon()
