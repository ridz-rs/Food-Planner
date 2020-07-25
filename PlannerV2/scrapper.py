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
            options1_count = 0
            for option in options1:
                self.check_arrow(options1_count)
                options1 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') # [donuts,timbits,muffins,bakedgoods]
                print("Line 24: ", option1texts, options1_count)
                try:  # wait until the category is clickable
                    to_click1 = WebDriverWait(self.driver, 10).\
                        until(expected_conditions.element_to_be_clickable((By.XPATH, '//div[contains(text(),\"{0}\")]'\
                            .format(option1texts[options1_count]))))
                    self.driver.execute_script("arguments[0].click()", to_click1)
                except TimeoutException:
                    to_click = self.driver.find_element_by_xpath("//div[contains(text(), \'{}\')]".format(option1texts[options1_count]))
                    print(to_click.text)
                    break
                sleep(3)
                options2 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') #[Yeastdonuts,cakedonuts,filleddonuts,other]
                inner_option2texts = [opt.text for opt in options2]
                option2_count = 0
                sleep(3)
                for option2 in options2:
                    self.check_arrow(option2_count)
                    options2 = self.driver.find_elements_by_class_name('taggedNutCalCatProd')
                    print("Line 39: ", inner_option2texts, option2_count)
                    try:
                        to_click2 = WebDriverWait(self.driver, 20).\
                            until(expected_conditions.element_to_be_clickable((By.XPATH, "//div[contains(text(),\'{}\')]"\
                                .format(inner_option2texts[option2_count]))))
                    except TimeoutException:
                        to_click = self.driver.find_element_by_xpath("//div[contains(text(), \'{}\')]".format(inner_option2texts[option2_count]))
                        print(to_click.text)
                        exit()
                    self.driver.execute_script("arguments[0].click()", to_click2)
                    sleep(3)
                    is_deepest = True
                    try:
                        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click() # check if it has a page to close
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
                    sleep(3)
                back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
                self.driver.execute_script("arguments[0].click()", back_button)
                # options1 = options1[1:]
                options1_count += 1 
                sleep(3)    
            back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
            self.driver.execute_script("arguments[0].click()", back_button)
            sleep(3)

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
        if len(options3)==1:
            self.data_dict[self.driver.find_element_by_id('search-item-title')]=self.driver.find_element_by_id('cal')
            try:
                self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click() # closes donut page
            except:
                close_button = WebDriverWait(self.driver, 10).\
                    until(expected_conditions.element_to_be_clickable\
                        ((By.XPATH, '/html/body/div[2]/div[3]/div[2]/div/div[1]/img')))
                close_button.click()
            return None
        next_button = WebDriverWait(self.driver, 10).\
            until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Next')))
        while(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Next'))):
            self.data_dict[self.driver.find_element_by_id('search-item-title')]=self.driver.find_element_by_id('cal')
            # loads donut data in data_dict
            self.driver.execute_script("arguments[0].click()", next_button)
            sleep(3)
            try:
                next_button = WebDriverWait(self.driver, 10).\
                until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, 'Next')))
            except TimeoutException:
                break
        self.data_dict[self.driver.find_element_by_id('search-item-title')]=self.driver.find_element_by_id('cal')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click() # closes donut page
        sleep(3)
        length = len(list(self.data_dict.keys()))
        print(length)   

    def check_arrow(self, num_completed):
        if num_completed==3:
            try:
                self.driver.find_element_by_class_name("bx-next").click()
                print("clicks on arrow")
            except:
                print("Could not find next arrow")

        
bot = timsbot()
sleep(3)
tags = bot.driver.find_elements_by_class_name('taggedNutCalCatProd') # [bakedgoods,breakfast,lunch,beverages]
tag_names = [tag.text for tag in tags]
tag_count = 0
sleep(3)
count =0
for tag in tags:
    try:
        tag_target = WebDriverWait(bot.driver, 20).until\
            (expected_conditions.element_to_be_clickable\
                ((By.LINK_TEXT,'{}'.format(tag_names[count]))))
        bot.driver.execute_script("arguments[0].click()", tag_target)
    except:
        print("couldn't click on {}".format(tag_names[count]))
    # tag.click()
    sleep(3)
    if count==0:
        bot.baked_goods()
    elif count ==1:
        # bot.breakfast()
        bot.baked_goods()
    elif count == 2:
        # bot.lunch()
        bot.baked_goods()
    elif count==3:
        # bot.beverage()
        bot.baked_goods()
    else:
        break
    count += 1
print(bot.data_dict)





            
