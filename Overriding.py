class Parent:

    def details(self):
        print("Parent Class overriding")

class Child(Parent):
    
    def details(self):
        print("Child class overriding")

obj=Parent()
obj.details()
