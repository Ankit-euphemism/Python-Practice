# 1.
# for i in range(1,101):
#     if(i%3!=0 and i%5!=0):
#         print(i)
        
# 2.

# age= int(input("Enter your age:- "))
# def calcAge(age):
#     if(age<25):
#         return("Junior")
#     if(age>=25 and age<=45):
#         return("Adult")
#     else:
#         return("Senior")
        
# print(calcAge(age))

# 3.
num= int(input("Enter your number:- "))

def even(num):
    for i in range(num+1):
        if i%2==0:
            print(i)

# for i in range(1,num):
#     print(even(i))

even(num)