class Employee:
    
    new_company="sk28"

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def show_details(self):
        print(f"The name is {self.name},the salary is {self.salary}")

    @classmethod
    def class_method(cls,new_company):
        cls.new_company=new_company
        print(f"Company name  is {cls.new_company}")

    @staticmethod
    def static_method(salary):
        if salary>=0:
            return True
        else:
            return False


 

obj1=Employee("Sayooj",25000)
obj1.show_details()
Employee.class_method("SK")
print(Employee.static_method(25000))

obj2=Employee("Akhil",35000)
obj2.show_details()
Employee.class_method("AK")
print(Employee.static_method(35000))

obj3=Employee("Ram",24000)
obj3.show_details()
Employee.class_method("RK")
print(Employee.static_method(24000))