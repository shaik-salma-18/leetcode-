class emp:
    def getdetails(self):
        self.name = input("Enter employee name: ")
        self.manager = input("Enter manager name: ")
        self.dept = input("Enter department: ")
        self.exp = int(input("Enter years of experience: "))
        self.score = int(input("Enter score out of 100: "))

    def check(self):
        if self.exp > 5 and self.score >= 60:
            print("Eligible for Promotion")
        else:
            print("Not Eligible for Promotion")

    def display(self):
        print("\n--- Employee Details ---")
        print("Employee Name:", self.name)
        print("Manager Name:", self.manager)
        print("Department:", self.dept)
        print("Experience:", self.exp, "years")
        print("Score:", self.score, "/100")
        self.check()


e = emp()
e.getdetails()
e.display()