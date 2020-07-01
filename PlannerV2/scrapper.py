from selenium import webdriver
from time import sleep

class timsbot:
    def __init__(self):
        print("starts init")
        self.driver = webdriver.Chrome(executable_path="C:/Users/Riddhesh/Downloads/chromedriver_win32/chromedriver.exe")
        self.driver.get("https://company.timhortons.com/ca/en/menu/nutrition-and-wellness.php")
        print("completes init")
        sleep(2)
        self.data_dict = {}
        
    def baked_goods(self):
        # sleep(5)
        # print("starts")
        # for i in first:
        #     i.click()
        #     sleep(5)
            length = 0
            options1 = self.driver.find_elements_by_class_name('taggedNutCalCatProd')
            for option in options1:
                option.click()
                sleep(5)
                options2 = self.driver.find_elements_by_class_name('taggedNutCalCatProd')
                sleep(5)
                for option2 in options2:
                    option2.click()
                    sleep(5)
                    options3 = self.driver.find_elements_by_class_name('taggedNutCalCatProd')
                    for option3 in options3:
                        if length%4==0 and length!=0:
                            sleep(5)
                            self.driver.find_element_by_link_text('Next').click() 
                        sleep(5)
                        option3.click()
                        sleep(5)
                        self.data_dict[self.driver.find_element_by_id('search-item-title')]=self.driver.find_element_by_id('cal')
                        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click()
                        sleep(5)
                        length = len(list(self.data_dict.keys()))
                        print(length)
                    self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a').click()
                    sleep(5)
                self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a').click()
                sleep(5)
            self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a').click()
            sleep(5)

    def breakfast(self):
        pass
    
    def lunch(self):
        pass

    def beverage(self):
        pass

bot = timsbot()
sleep(5)
tags = bot.driver.find_elements_by_class_name('taggedNutCalCatProd')
sleep(5)
count =1
for tag in tags:
    tag.click()
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





            
