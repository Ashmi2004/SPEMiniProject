
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
 

class CalcTest(unittest.TestCase):
 
    def setUp(self):
        cservice=webdriver.ChromeService(executable_path='/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome(service = cservice)

 
    def test_search_in_python_org(self): 
        driver = self.driver
        driver.get("file:///home/asmita/Documents/SPEMiniProject/calculator.html")
        time.sleep(2)
        inputscreen = driver.find_element(By.XPATH,"/html/body/div/form/div[1]/input")
        inputscreen.send_keys("2+2")
        equals = driver.find_element(By.XPATH,"/html/body/div/form/div[2]/div[4]/input[4]")
        equals.send_keys(Keys.ENTER)
        #inputscreen.get_attribute("value")
        self.assertEqual(inputscreen.get_attribute("value"), "4")


    def tearDown(self):
        self.driver.close()
        self.driver.quit()
 
if __name__ == "__main__":
    unittest.main()
