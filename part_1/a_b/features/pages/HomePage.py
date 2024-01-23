from selenium.webdriver.common.by import By
from utilities import ConfigReader
import time

KEY_WORD = ConfigReader.read_configuration("Search","key_word")

TIME_TO_WAIT = int(ConfigReader.read_configuration("Time","wait"))

class HomePage:

    def __init__(self,driver):
        self.driver = driver
    
    my_class_name_search_field = "q"
    my_class_name_search_button = "btnK"
    my_class_name_web_site_names = "LC20lb.MBeuO.DKV0Md"
    

    def type_test_automation(self):
        self.driver.find_element(By.NAME , self.my_class_name_search_field).send_keys(KEY_WORD)
        time.sleep(TIME_TO_WAIT)
    
    def click_search_button(self):
        self.driver.find_element(By.NAME,self.my_class_name_search_button).click()
        time.sleep(TIME_TO_WAIT)
    
    def scroll_down(self, times):
        for i in range(0,times):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/3);")
            time.sleep(TIME_TO_WAIT)
    
    def get_web_site_names(self):
        return self.driver.find_elements(By.CLASS_NAME,self.my_class_name_web_site_names)
    
    def click_first_result(self):
        self.driver.find_element(By.CLASS_NAME,self.my_class_name_web_site_names).click()
        time.sleep(TIME_TO_WAIT)
    