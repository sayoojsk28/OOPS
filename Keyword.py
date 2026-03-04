class Student:

    def details(self,**kwargs):
        print(f"The name is {kwargs["name"]},Age is {kwargs["age"]},Place is {kwargs["place"]},Degree is {kwargs["Degree"]}")

obj=Student()
obj.details(name="sayooj",age=22,place="Kannur",Degree="BCA")
