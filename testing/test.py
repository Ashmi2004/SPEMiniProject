
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class CalcTest(unittest.TestCase):
 
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--start-maximized")
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--ignore-certificate-errors')
        cservice=Service()
        self.driver = webdriver.Chrome(service=cservice, options=options)
        #self.driver.get("http://172.16.144.32:8090")

 
    def test_addition(self): 
        driver = self.driver
        driver.get("http://172.16.144.32:8090")
        print(driver.title)
        inputscreen = driver.find_element(By.NAME,"displayResult")
        inputscreen.send_keys("2+2")
        equals = driver.find_element(By.CLASS_NAME,"red")
        equals.send_keys(Keys.ENTER)
        #inputscreen.get_attribute("value")
        #inputscreen = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/input")
        #inputscreen.send_keys("2+2")
        #time.sleep(7)
        #equals = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div[4]/input[4]")
        #equals.send_keys(Keys.ENTER)
        self.assertEqual(inputscreen.get_attribute("value"), "4")

    def test_subtraction(self):
        driver = self.driver
        driver.get("http://172.16.144.32:8090")
        inputscreen = driver.find_element(By.NAME,"displayResult")
        inputscreen.send_keys("6-2")
        equals = driver.find_element(By.CLASS_NAME,"red")
        equals.send_keys(Keys.ENTER)
        self.assertEqual(inputscreen.get_attribute("value"), "4")

    def test_multiplication(self):
        driver = self.driver
        driver.get("http://172.16.144.32:8090")
        inputscreen = driver.find_element(By.NAME,"displayResult")
        inputscreen.send_keys("10*2")
        equals = driver.find_element(By.CLASS_NAME,"red")
        equals.send_keys(Keys.ENTER)
        self.assertEqual(inputscreen.get_attribute("value"), "20")

    def test_division(self):
        driver = self.driver
        driver.get("http://172.16.144.32:8090")
        inputscreen = driver.find_element(By.NAME,"displayResult")
        inputscreen.send_keys("6/3")
        equals = driver.find_element(By.CLASS_NAME,"red")
        equals.send_keys(Keys.ENTER)
        self.assertEqual(inputscreen.get_attribute("value"), "2")

    def test_factorial(self):
        driver = self.driver
        driver.get("http://172.16.144.32:8090")
        inputscreen = driver.find_element(By.NAME,"b3")
        inputscreen.send_keys(Keys.ENTER)
        inputscreen = driver.find_element(By.NAME,"fact")
        inputscreen.send_keys(Keys.ENTER)
        inputscreen = driver.find_element(By.NAME,"displayResult")
        self.assertEqual(inputscreen.get_attribute("value"), "6")

    def test_squareRoot(self):
        driver = self.driver
        driver.get("http://172.16.144.32:8090")
        inputscreen = driver.find_element(By.NAME,"b2")
        inputscreen.send_keys(Keys.ENTER)
        inputscreen = driver.find_element(By.NAME,"b5")
        inputscreen.send_keys(Keys.ENTER)
        inputscreen = driver.find_element(By.NAME,"sqrt")
        inputscreen.send_keys(Keys.ENTER)
        inputscreen = driver.find_element(By.NAME,"displayResult")
        self.assertEqual(inputscreen.get_attribute("value"), "5")

    def test_logarithmic(self):
        driver = self.driver
        driver.get("http://172.16.144.32:8090")
        inputscreen = driver.find_element(By.NAME,"b1")
        inputscreen.send_keys(Keys.ENTER)
        inputscreen = driver.find_element(By.NAME,"log")
        inputscreen.send_keys(Keys.ENTER)
        inputscreen = driver.find_element(By.NAME,"displayResult")
        self.assertEqual(inputscreen.get_attribute("value"), "0")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
 
if __name__ == "__main__":
    unittest.main()
