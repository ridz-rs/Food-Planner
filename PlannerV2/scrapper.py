from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class timsbot:
    def __init__(self):
        print("starts init")
        self.driver = webdriver.Chrome(executable_path="C:/Users/Riddhesh/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://company.timhortons.com/ca/en/menu/nutrition-and-wellness.php")
        print("completes init")
        # self.driver.fullscreen_window()
        sleep(2)
        self.data_dict = {}
        
    def baked_goods(self):
        # sleep(5)
        # print("starts")
        # for i in first:
        #     i.click()
        #     sleep(5)
            length = 0
            options1 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') # [donuts,timbits,muffins,bakedgoods]
            for option in options1:
                self.driver.execute_script("arguments[0].click()", option)
                # option.click()
                sleep(5)
                options2 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') #[Yeastdonuts,cakedonuts,filleddonuts,other]
                options2_xpaths = [element.get_attribute("xpath") for element in options2]
                option2_count = 0
                print(options2_xpaths)
                sleep(5)
                for option2 in options2:
                    to_click = WebDriverWait(self.driver, 20).\
                        until(expected_conditions.element_to_be_clickable((By.XPATH, options2_xpaths[option2_count])))
                    self.driver.execute_script("arguments[0].click()", to_click)
                    sleep(5)
                    options3 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') #[AppleFritter, Chocolate dip, Maple Dip...]
                    option3 = options3[0]
                    self.driver.execute_script("arguments[0].click()", option3) # clicks on the donut
                    next_button = WebDriverWait(self.driver, 10).\
                        until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Next')))
                    while(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Next'))):
                        self.data_dict[self.driver.find_element_by_id('search-item-title')]=self.driver.find_element_by_id('cal')
                        # loads donut data in data_dict
                        self.driver.execute_script("arguments[0].click()", next_button)
                        sleep(5)
                        try:
                            next_button = WebDriverWait(self.driver, 10).\
                            until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Next')))
                        except TimeoutException:
                            break
                    self.data_dict[self.driver.find_element_by_id('search-item-title')]=self.driver.find_element_by_id('cal')
                    self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click() # closes donut page
                    sleep(5)
                    length = len(list(self.data_dict.keys()))
                    print(length)
                    back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
                    self.driver.execute_script("arguments[0].click()", back_button)
                    options2 = options2[1:]
                    option2_count += 1
                    sleep(5)
                back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
                self.driver.execute_script("arguments[0].click()", back_button)
                options1 = options1[1:]
                sleep(5)    
            back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
            self.driver.execute_script("arguments[0].click()", back_button)
            sleep(5)

    def breakfast(self):
        pass
    
    def lunch(self):
        pass

    def beverage(self):
        pass

    def wait_multiple(self, outer_element, class_name):
        pass


bot = timsbot()
sleep(5)
tags = bot.driver.find_elements_by_class_name('taggedNutCalCatProd') # [bakedgoods,breakfast,lunch,beverages]
sleep(5)
count =1
for tag in tags:
    bot.driver.execute_script("arguments[0].click()", tag)
    # tag.click()
    sleep(5)
    if count==1:
        bot.baked_goods()
    elif count ==2:
        bot.breakfast()
    elif count == 3:
        bot.lunch()
    elif count==4:
        bot.beverage()
    else:
        break
    count += 1





            
