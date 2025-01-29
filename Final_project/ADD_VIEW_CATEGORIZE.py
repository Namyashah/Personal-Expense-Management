from datetime import date
expense_list = []
class Add_View_Categorize:
    def __init__(self):
        while True:
            print("Expense Editor Options: ")
            print("1.Add An Expense.")
            print("2.View Expense.")
            print("3.Categorize Expense.")
            print("4.Total_Expense.")
            print("5.Back To Main Menu.")

            self.choice = int(input("Enter your Choice = "))
            
            if self.choice==1:
                self.add_expense()
            elif self.choice==2:
                self.view_expense()
            elif self.choice==3:
                self.category_expense()
            elif self.choice==4:
                self.total_expense()
            elif self.choice==5:
                print("Loading Main Menu!")
                print("=====================================")
                break
            else:
                print("Invalid Input!Enter Proper Input")
                print("=====================================")
    def add_expense(self):
        dict = {}
        self.expense_no = int(input("Enter The Expense_no = "))
        self.amount = float(input("Enter Your Expense Amount = "))
        self.category = input("Enter Expense Category = ")
        self.date = date.today().strftime(r"%d-%m-%Y")
        dict["Expense_no"] = self.expense_no
        dict["Amount"] = self.amount
        dict["Category"] = self.category
        dict["Date"] = self.date
        for i in expense_list:
            if dict["Expense_no"]==i["Expense_no"]:
                print("Expense_no Can't Be same!")
                print("=============================")
                break
        else:
            if dict["Amount"]>0:
                expense_list.append(dict)
                print("Expense Added Successfull!!")
                print("====================================")
            else:
                print("Amount Should Be Postive!")
                print("=====================================")
            print(expense_list)
    def view_expense(self):
        print("Showing All Your Expenses:")
        if expense_list:
            for i in expense_list:
                print(f"Expense_no = {i["Expense_no"]}")
                print(f"Amount = {i["Amount"]}")
                print(f"Category = {i["Category"]}")
                print(f"Date = {i["Date"]}")
                print("======================================")
            save_file = input("Do you want to save the file (yes\no) = ").lower()
            file_name = input("Please enter The Name OF file as (.csv) = ")
            if save_file=="yes":
                for expense in expense_list:
                    with open(file_name,"a",encoding="utf-8") as file:
                        file.write(f"Expense No = {expense["Expense_no"]},Amount = {expense["Amount"]},Category = {expense["Category"]},Date = {expense["Date"]}\n")
                print("File Saved Successfully!")
                print("=============================")
            else:
                print("File Has Not Been Saved!")
                print("========================")
        else:
            print("Your Expense List Is Empty!")
            print("======================================")
    def category_expense(self):
        if expense_list:
            while True:
                print("Choose An Operations:")
                print("1.Show Categort Vise.")
                print("2.Back To Page-2")

                self.choice = int(input("Enter your choice = "))

                if self.choice==1:
                    category_input = input("Enter the category You want to search = ")
                    for i in expense_list:
                        if category_input==i["Category"]:
                            print(f"Expense_no = {i["Expense_no"]}")
                            print(f"Amount = {i["Amount"]}")
                            print(f"Category = {i["Category"]}")
                            print(f"Date = {i["Date"]}")
                            print("======================================")
                elif self.choice==2:
                    print("Loading Page-2.")
                    print("========================")
                    break
                else:
                    print("Invalid Input!Enter Proper Input!")
                    print("==================================")
        else:
            print("Your List Is Empty!")
            print("===================================")
    def total_expense(self):
        c = 0
        for i in expense_list:
            c = c + i["Amount"]
        print(f"Total_expense = {c}")
        print("======================================")