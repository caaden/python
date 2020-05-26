
class Person:
    # initializing the variables
    name = ""
    age = 0

    # defining constructor
    def __init__(self, person_name, person_age):
        self.name = person_name
        self.age = person_age

        # defining class methods

    def show_name(self):
        print(self.name)

    def show_age(self):
        print(self.age)


# definition of subclass starts here
class Student(Person):
    studentId = ""

    def __init__(self, student_name, student_age, student_id):
        Person.__init__(self, student_name, student_age)
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # returns the value of student id

# definition of subclass starts here
class SuperStudent(Person):
    studentId = ""

    def __init__(self, student_name, student_age, student_id):
        #note, don't refer to parent class at all... not even passing self.
        super().__init__(student_name, student_age)
        self.studentId = student_id

    def get_id(self):
        return self.studentId  # returns the value of student id


# end of subclass definition

def main():
    # Create an object of the superclass
    person1 = Person("Richard", 23)
    # call member methods of the objects
    person1.show_age()
    # Create an object of the subclass using conventional inheritance
    student1 = Student("Max", 22, "102")
    print(student1.get_id())
    student1.show_name()
    # Create an object using super()
    student2=SuperStudent('Chris',43,"001")
    student2.show_name()
    student2.show_age()
    print(student2.name," is: ",student2.age, " years old.")

if __name__=="__main__":
    main()
    