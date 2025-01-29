from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class OnlineTracker:
    def tracker(self):
        while True:
            print("Choose An Operations:")
            print("1.Online Expense tracker.")
            print("2.Back To Main Menu.")

            self.choice = int(input("Enter your choice = "))

            if self.choice==1:
                my_options = Options()
                my_options.add_experimental_option("detach",True)
                my_options.add_argument("--start-maximized")

                driver = webdriver.Chrome(options=my_options)
                url = "https://accounts.zoho.in/signin?servicename=ZohoExpense&signupurl=https://www.zoho.com/in/expense/signup/"
                driver.get(url)
                sleep(3)

                email_address = driver.find_element(By.NAME,"LOGIN_ID")
                email_address.send_keys("namyashah0508@gmail.com")
                next_button = driver.find_element(By.XPATH,"/html/body/div[5]/div[2]/div[3]/div[4]/form[1]/button")
                next_button.click()

                password = driver.find_element(By.NAME,"PASSWORD")
                password.send_keys("nam@0508")
                sign_in = driver.find_element(By.XPATH,"html/body/div[5]/div[2]/div[3]/div[4]/form[1]/button")
                sign_in.click()

                if driver.title=="Getting Started|Zoho Expense":
                    print("Login Successfully!")
                    print("=============================")
                    
                else:
                    print("Login Unsucessfull!")
                    print("=============================")

            elif self.choice==2:
                print("Loading Main Menu!")
                print("Please Wait!")
                print("==============================")
                break
            else:
                print("Invalid Input!Enter Proper Input!")
                print("=====================================")
o1 = OnlineTracker()
o1.tracker()