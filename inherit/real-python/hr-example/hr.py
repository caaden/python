#%% Dependencies
from abc import ABC, abstractmethod
# Abstract base classes exist to be inherited, but never instantiated. 
# Python provides the abc module to define abstract base classes.

#%% Payroll Class requires employees
class PayrollSystem:
    def calculate_payroll(self,employees):
        print('Calculating payroll.')
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')
            print('')
            
#%% Employees
#By inheriting from ABC, Employee can never be instantiated.
class Employee(ABC):
    def __init__(self,id,name):
        # constructor includes an id and name
        self.id=id
        self.name=name
    # abstractmethod decorator requires overriding the decorated method
    @abstractmethod
    def calculate_payroll(self):
        pass
             
#SalaryEmployee
class SalaryEmployee(Employee):
    def __init__(self,id,name,weekly_salary):
        #use super() to reference the base class
        super().__init__(id,name)
        #initialize new object
        self.weekly_salary=weekly_salary
    def calculate_payroll(self):
        return self.weekly_salary
    
#HourlyEmployee
class HourlyEmployee(Employee):
    def __init__(self,id,name,hours_worked,hour_rate):
        super().__init__(id,name)
        self.hours_worked=hours_worked
        self.hour_rate=hour_rate
    def calculate_payroll(self):
        return self.hours_worked*self.hour_rate        
# CommissionEmployee
class CommissionEmployee(SalaryEmployee):
    def __init__(self,id,name,weekly_salary,commission):
        super().__init__(id,name,weekly_salary)
        self.commission=commission
    def calculate_payroll(self):
        #user super to reference base calss
        fixed=super().calculate_payroll()
        return fixed+self.commission
    
#%% Unit Test
salary_employee=SalaryEmployee(1,"John Smith",1500)
hourly_employee=HourlyEmployee(2,"Jane Doe",40,15)
commission_employee=CommissionEmployee(3,"Kevin Bacon",1000,750)
payroll_system=PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee,hourly_employee,commission_employee
])

# %%
