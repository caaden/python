class Parent: #define parent class
    parentAttr=100
    def __init__(self):
        print('Parent Constructor')
    def parentMethod(self):
        print('Calling parent method')
    def setAttr(self,attr):
        Parent.parentAttr=attr
    def getAttr(self):
        print("Parent attribute: ",Parent.parentAttr)

class Child(Parent): #define child class
    def __init__(self):
        print("Child constructor")
    def childMethod(self):
        print('Calling child method')
        


c=Child()
c.childMethod()
c.parentMethod()
c.setAttr(501)
c.getAttr()