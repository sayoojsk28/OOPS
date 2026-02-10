def x(a):
    if a==0|a==1 :
        return 1
    else:
        return a*(x(a-1))
        
    

    
a=int(input("Enter the number:"))

print(x(a))
        
  


