from ADD_VIEW_CATEGORIZE import Add_View_Categorize
from FETCH_DISPLAY_SCRAPPER import NewsScrapper
from AUTOMATION_ONLINE_TRACKER import OnlineTracker
from ANALYZE_SPENDING import SpendingHabits
class FinanceManager:
    def __init__(self):
        print("============================================================")
        print("Welcome To Personal Finance Management and Automation System")
        print("============================================================")
        while True:
            print("Choose An Operation from The Following:")
            print("1.Add,View and Categorize Expense.")
            print("2.Analyze Spending habits.")
            print("3.Fetch And Display The Latest Financial News.")
            print("4.Automation of Recurring Expenses into an online Finance Tracker.")
            print("5.Exit.")

            self.choice = int(input("Enter Your choice = "))

            if self.choice==1:
                print("==============================")
                Add_View_Categorize()
            elif self.choice==2:
                print("==============================")
                SpendingHabits()
            elif self.choice==3:
                print("===============================")
                NewsScrapper()
            elif self.choice==4:
                print("===============================")
                OnlineTracker()
            elif self.choice==5:
                self.choice = input("Do You Want To Exit Personal Finance Management(yes\no) = ").lower()
                if self.choice=="yes":
                    print("Thank You For Using Personal Finance Management and Automation System!")
                    print("Visit Again")
                    print("Goodbyee!!")
                    print("==================================================")
                    break
                else:
                    print("Loading The Same Page Please Wait Few Seconds!")
                    print("============================================")
            else:
                print("Invalid Input!Enter Proper Input!!")
                print("==========================================")
f1 = FinanceManager()