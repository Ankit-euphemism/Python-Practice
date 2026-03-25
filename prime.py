n= int(input("Enter your number:- "))

flag= False
for i in range(n):
    if(i==0 or i==1):
        continue
    
    if(n%i!=0):
        flag= True
        print("Prime number")
    else:
        print("Not Prime Number")
    