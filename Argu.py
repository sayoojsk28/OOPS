class Multi:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def mul(self):
        c=self.a*self.b
        return c

    def sub(self):
        c=self.a-self.b
        print(c)

    def add(self):
        c=self.a+self.b
        print(c)

    def div(self):
        c=self.a/self.b
        print(c)
        
obj=Multi(8,2)
print(obj.mul())
obj.sub()
obj.add()
obj.div()        