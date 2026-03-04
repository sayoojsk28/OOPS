
def add(a,b,c):

    print(a+b)

def sub(a,b,c):
    print(a-b)

def mul(a,b,c):
    print(a*b)

def div(a,b,c):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Number can't be divide by zero")

    
       
    

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=input("Enter operator:")
if c=="+":
    add(a,b,c)
elif c=="-":
    sub(a,b,c)
elif c=="*":
    mul(a,b,c)
elif c=="/":
    div(a,b,c)
else:
    print("Invalid Syntax")

    Doc