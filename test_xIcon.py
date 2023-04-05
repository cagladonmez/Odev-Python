# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestXIcon():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_xIcon(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(825, 824)
    WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "*[data-test=\"login-button\"]")))
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form_group:nth-child(1) > .svg-inline--fa")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form_group:nth-child(2) path")
    assert len(elements) > 0
    self.driver.find_element(By.CSS_SELECTOR, ".fa-times").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form_group:nth-child(1) path")
    assert len(elements) == 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".form_group:nth-child(2) path")
    assert len(elements) == 0
  
