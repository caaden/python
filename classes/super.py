#%% base class
class MyParentClass(object):
    def __init__(self):
        pass

#%% derived class
class SubClass(MyParentClass):
    def __init__(self):
        #%% derived class still needs to initialize the base class
        MyParentClass.__init__(self)

#%% derived class using super
# parent class no longer based on derived
class SubClassSuper(MyParentClass):
    def __init__(self):
        super()

#%%Shape Example

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


sq1=Square(12)
print(sq1.area())