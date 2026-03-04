class Student:

    count=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Student.count += 1

    def details(self):
        print(f"Name is {self.name} Age is {self.age} ")

    @classmethod
    def class_method(cls):
        print(f"Count is {cls.count}")

    @staticmethod
    def static_method(age):
        if age>=18:
            print("Adult")
        else:
            print("Minor")


    
obj=Student("SK",28)
obj.details()
Student.class_method()
Student.static_method(22)
obj1=Student("AK",34)
Student.class_method()
