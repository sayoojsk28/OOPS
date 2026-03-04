class Salary:

    def calculatesalary(self,salar):
        print(f"The salary is {salar}")

class PartTime(Salary):

    def calculatesalary(self,hourrate,hours):
        print(f"The salary is {hourrate*hours}")

class Freelancer(PartTime,Salary):

    def calculatesalary(self,project_cash,project_no):
        print(f"The salary is {project_cash*project_no}")
        

obj1=Salary()
obj1.calculatesalary(1200)
obj2=PartTime()
obj2.calculatesalary(200,10)
obj3=Freelancer()
obj3.calculatesalary(2500,5)
        
