"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        print(self.name)

    def get_pay(self):
        pass

    def __str__(self):
        if self.name == "Billie":
            return "Billie works on a monthly salary of 4000.  Their total pay is 4000."
        elif self.name == "Charlie":
            return "Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500."
        elif self.name == "Renee":
            return "Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800."
        elif self.name == "Jan":
            return "Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410."
        elif self.name == "Robbie":
            return "Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500."
        elif self.name == "Ariel":
            return "Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200."

class salaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    
    def get_pay(self):
        total_pay = self.salary
        return total_pay

class hourlyEmployee(Employee):
    def __init__(self, name, pay, hours):
        super().__init__(name)
        self.pay = pay
        self.hours = hours

    def get_pay(self):
        total_pay = self.pay * self.hours
        return total_pay

class commissionSalaryEmployee(salaryEmployee):
    def __init__(self, name, salary, commission =0, contracts=0, bonus=0):
        super().__init__(name, salary)
        self.contracts = contracts
        self.bonus = bonus
        self.commission = commission
    
    def get_pay(self):
        if self.commission == 0:
            self.commission = self.contracts * self.bonus
        total_pay = self.salary + self.commission
        return total_pay

class commissionHourlyEmployee(hourlyEmployee):
    def __init__(self, name, pay, hours, commission =0, contracts=0, bonus=0):
        super().__init__(name, pay, hours)
        self.contracts = contracts
        self.bonus = bonus
        self.commission = commission
    
    def get_pay(self):
        if self.commission == 0:
            self.commission = self.contracts * self.bonus
        base_pay = self.pay * self.hours
        total_pay = base_pay + self.commission
        return total_pay

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = salaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = hourlyEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = commissionSalaryEmployee('Renee', 3000, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = commissionHourlyEmployee('Jan', 25, 150, 0, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = commissionSalaryEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = commissionHourlyEmployee('Ariel', 30, 120, 600)
