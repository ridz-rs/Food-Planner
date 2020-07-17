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
        self.driver = webdriver.Chrome(executable_path="C:/Users/Riddhesh/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://company.timhortons.com/ca/en/menu/nutrition-and-wellness.php")
        # self.driver.fullscreen_window()
        sleep(2)
        self.data_dict = {}
        
    def baked_goods(self):
            length = 0
            options1 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') # [donuts,timbits,muffins,bakedgoods]
            option1texts = [opt.text for opt in options1]
            print(option1texts)
            options1_count = 0
            for option in options1:
                try:
                    print("goes in 1st try")
                    to_click1 = WebDriverWait(self.driver, 10).\
                        until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[contains(text(),\"{0}\")]'\
                            .format(option1texts[options1_count]))))
                    self.driver.execute_script("arguments[0].click()", to_click1)
                except TimeoutException:
                    to_click = self.driver.find_element_by_xpath("//div[contains(text(), \'{}\')]".format(option1texts[options1_count]))
                    print(to_click.text)
                # option.click()
                sleep(5)
                options2 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') #[Yeastdonuts,cakedonuts,filleddonuts,other]
                inner_option2texts = [opt.text for opt in options2]
                print(inner_option2texts)
                option2_count = 0
                sleep(5)
                for option2 in options2:
                    try:
                        to_click2 = WebDriverWait(self.driver, 20).\
                            until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[contains(text(),\'{}\')]"\
                                .format(inner_option2texts[option2_count]))))
                    except TimeoutException:
                        to_click = self.driver.find_element_by_xpath("//div[contains(text(), \'{}\')]".format(inner_option2texts[option2_count]))
                        print(to_click.text)
                    self.driver.execute_script("arguments[0].click()", to_click2)
                    sleep(5)
                    """
                        TODO: call read_inner_options() appropriately when the opened page is the innermost one
                    """
                    is_deepest = True
                    try:
                        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click()
                    except:
                        print("excepts!")
                        is_deepest = False
                    finally:
                        self.read_inner_items()
                        if is_deepest:
                            break
                    back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
                    self.driver.execute_script("arguments[0].click()", back_button)
                    # options2 = options2[1:]
                    option2_count += 1
                    sleep(5)
                back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
                self.driver.execute_script("arguments[0].click()", back_button)
                # options1 = options1[1:]
                options1_count += 1 
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
    def read_inner_items(self):
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
print(bot.data_dict)





            
