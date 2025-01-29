import requests
from bs4 import BeautifulSoup
class NewsScrapper:
    def news(self):
        while True:
            print("Choose An Operations:")
            print("1.Financial News.")
            print("2.back To Main Menu.")

            self.choice = int(input("Enter your choice = "))

            if self.choice==1:  
                self.news_fetch = input("Do You Want To Get Financial News(yes\no) = ").lower()
                if self.news_fetch=="yes":
                    url = "https://www.livemint.com/latest-news"
                    try:
                        response = requests.get(url)
                        
                        if response.status_code==200:
                            soup = BeautifulSoup(response.text,"html.parser")
                            head = soup.select("h2.headline a")
                            if head:
                                print("Fetching News From Websites Please Wait a minute!")
                                print("===============================")
                                for i in range(10):
                                    print(f"Headlines = {head[i].text.strip()}")
                                    print("=================================")
                                print("Financial News are Displayed")
                                print("After Reading Please Give Us Feedback!")
                                print("===================================")
                            else:
                                print("No Headlines Found Sorry!")
                                print("================================")
                        else:
                            print("Website Error-404!!")
                            print("==================================")
                    except Exception as e:
                        print("There Was Some Error While Loading the Webiste Contact Us Later!")
                        print("=======================================================")
                else:
                    print("Invalid Input!Enter Proper Input!")
                    print("==========================================")
            elif self.choice==2:
                print("Loading Main Menu!")
                print("Please Wait!")
                print("======================")
                break
            else:
                print("Invalid Input!Enter Proper Input!")
                print("==========================")