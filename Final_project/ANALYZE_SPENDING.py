import subprocess as sub
import time
class SpendingHabits:
    def analyzing(self):
        while True:
            print("Choose An Operations:")
            print("1.Visualize Through Excel Bar chart.")
            print("2.back To Main Menu.")

            self.choice = int(input("Enter your choice = "))

            if self.choice==1:
                file_path = r"C:\Users\victus\OneDrive\文档\Red and White Lab work\expense.csv"
                sub.Popen(["start","excel",file_path],shell=True)
                print("Opening Excel Please!")
                print("===================================")
                time.sleep(3)
            elif self.choice==2:
                print("Loading Main Menu!")
                print("Please Wait!")
                print("================================")
                break
            else:
                print("Invalid Output!Enter Proper Input!")
                print("===================================")