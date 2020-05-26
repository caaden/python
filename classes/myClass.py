class Employee:
    #variable shared by all Employee objects
    empcount=0

    #constructor
    def __init__(self,name,salary): 
        self.name=name
        self.salary=salary
        Employee.empcount+=1

    def displayCount(self):
        print('Total employees:'+Employee.empcount)

    def displayEmp(self):
        print('Name: ',self.name,', Salary: ',self.salary)


#This would create first object of Employee class
emp1 = Employee("Zara", 2000)
#This would create second object of Employee class
emp2 = Employee("Manni", 5000)

emp1.displayEmp()
emp2.displayEmp()
print('Total employees: ',Employee.empcount)