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
        sleep(2)
        is_deepest = False
        try:  # base case
            self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click()
            is_deepest = True
        except:
            options = self.driver.find_elements_by_class_name('taggedNutCalCatProd')
            option_texts = [opt.text for opt in options]
            for i in range(len(option_texts)):
                self.check_arrow(i)
                sleep(2)
                options = self.driver.find_elements_by_class_name('taggedNutCalCatProd') #get categories after scrolling
                option_texts = [opt.text for opt in options]
                print(option_texts[i], i, len(option_texts))
                sleep(2)
                try:
                    to_click = WebDriverWait(self.driver, 10)\
                        .until(expected_conditions.element_to_be_clickable\
                            ((By.XPATH, '//div[contains(text(),\"{0}\")]'.format(option_texts[i]))))
                    self.driver.execute_script("arguments[0].click()", to_click) # click on category
                    try:
                        print("recurses")
                        to_break = self.data_surfer() # carries out the same code for inner categories
                        if to_break:
                            print("breaks", option_texts)
                            break
                    except Exception as e:
                        print("error at", option_texts[i])
                        print(e)
                        exit()
                except Exception as e:
                    print("could not click")
                    print(e)
                    break
                sleep(2)
            try:
                print("looks for back button")
                back_button = self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[1]/div[6]/div[2]/div/div[2]/div/a')
                self.driver.execute_script('arguments[0].click()', back_button) # goes back from the items page 
            except:
                print("no back button")
                return False
            print("Goes in outermost except")
        finally:
            if is_deepest:
                self.read_inner_elements()
                return True

    
    def check_arrow(self, num_completed):
        print("checks for arrow")
        if num_completed>=3:
            try:
                self.driver.find_element_by_class_name("bx-next").click()
                print("clicks on arrow")
            except:
                print("Could not find next arrow")

    def read_inner_elements(self):
        print("reader called")
        options3 = self.driver.find_elements_by_class_name('taggedNutCalCatProd') #[AppleFritter, Chocolate dip, Maple Dip...]
        option3 = options3[0]
        sleep(2)
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
                self.data_dict[self.driver.find_element_by_id('search-item-title').text] = self.driver.find_element_by_id('cal').text
                self.driver.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/div/div[1]/img').click() # closes donut page
                length = len(list(self.data_dict.keys()))
                print(length)
                return None
            self.data_dict[self.driver.find_element_by_id('search-item-title').text]=self.driver.find_element_by_id('cal').text
            # loads donut data in data_dict
            if next_button is not None:
                self.driver.execute_script("arguments[0].click()", next_button)
            sleep(2)


bot = timsbot()
try:
    bot.data_surfer()
except Exception as e:
    print(e)   
print(bot.data_dict)
try:
    with open('TimsData.csv', 'a') as fd:
        for key in self.data_dict:
            fd.writelines([key, '', self.data_dict[key]])
except Exception as e:
    print('Writing error')
    print(e)


