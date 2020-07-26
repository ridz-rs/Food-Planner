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
        sleep(2)
        self.data_dict = {}
    
    def data_surfer(self):
        sleep(3)
        is_deepest = False
        try:  # base case
            self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click()
            is_deepest = True
            return True
        except:
            options = self.driver.find_elements_by_class_name('taggedNutCalCatProd')
            option_texts = [opt.text for opt in options]
            option_count = 0
            for i in range(len(option_texts)):
                self.check_arrow(option_count)
                sleep(3)
                options = self.driver.find_elements_by_class_name('taggedNutCalCatProd')
                option_texts = [opt.text for opt in options]
                print(option_texts[option_count], option_count, len(option_texts))
                sleep(3)
                try:
                    to_click = WebDriverWait(self.driver, 10)\
                        .until(expected_conditions.element_to_be_clickable\
                            ((By.XPATH, '//div[contains(text(),\"{0}\")]'.format(option_texts[option_count]))))
                    self.driver.execute_script("arguments[0].click()", to_click)
                    try:
                        print("recurses")
                        to_break = self.data_surfer() # carries out the same code for inner categories
                        if to_break:
                            break
                        option_count += 1
                    except Exception as e:
                        print("error at", option_texts[option_count])
                        print(e)
                        exit()
                except Exception as e:
                    print("could not click")
                    print(e)
                    break
                sleep(3)
            print("Goes in outermost except")

        finally:
            if is_deepest:
                self.read_inner_elements()

    
    def check_arrow(self, num_completed):
        print("checks for arrow")
        if num_completed==3:
            try:
                self.driver.find_element_by_class_name("bx-next").click()
                print("clicks on arrow")
            except:
                print("Could not find next arrow")

    def read_inner_elements(self):
        print("reader called")
        options3 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') #[AppleFritter, Chocolate dip, Maple Dip...]
        option3 = options3[0]
        sleep(3)
        try:
            self.driver.execute_script("arguments[0].click()", option3) # clicks on the donut
        except:
            print("could not click on", option3.text)
        next_button = None
        for i in range(len(options3)):
            try:
                next_button = WebDriverWait(self.driver, 10).until\
                    (expected_conditions.element_to_be_clickable((By.LINK_TEXT,'Next')))
            except TimeoutException:
                print("could not find next button")
                break
            self.data_dict[self.driver.find_element_by_id('search-item-title')]=self.driver.find_element_by_id('cal')
            # loads donut data in data_dict
            self.driver.execute_script("arguments[0].click()", next_button)
            sleep(3)
        self.data_dict[self.driver.find_element_by_id('search-item-title')] = self.driver.find_element_by_id('cal')
        self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click() # closes donut page
        try:
            print("looks for back button")
            back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
            self.driver.execute_script('arguments[0].click()', back_button)
        except:
            print("no back button")
        sleep(3)
        length = len(list(self.data_dict.keys()))
        print(length)

bot = timsbot()
bot.data_surfer()   


