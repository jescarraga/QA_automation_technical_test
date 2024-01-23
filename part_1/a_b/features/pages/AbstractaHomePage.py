from selenium.webdriver.common.by import By
from utilities import ConfigReader
import time

TIME_TO_WAIT = int(ConfigReader.read_configuration("Time","wait"))

class AbstractaHomePage:

    def __init__(self,driver):
        self.driver = driver
    
    my_class_name_tittle_page = "post-title"

    def get_tittle_page(self):
        return self.driver.find_element(By.CLASS_NAME,self.my_class_name_tittle_page).text