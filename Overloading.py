class Calc:

    def add(self,*args):
        addi=sum(args)
        print(addi)

obj=Calc()
obj.add(1,2,4,6,7)
obj.add(4,6,8,3)
obj.add(4,7,8,5,4)

