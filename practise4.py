# Accept two integer values from the user; display the number which is smaller and the number
# which is bigger.

# num1=int(input("enter first number"))
# num2=int(input("enter second number"))

# if num1<num2:
#     print("smaller number",num1)
#     print("bigger number",num2)
# elif num1>num2:
#     print("smaller number",num2)
#     print("bigger number",num1)
# else:
#     print("both are equal",num1)    

# Accept one integer value from the user; check whether entered number is divisible by 5 or not.
# num=int(input("enter a number"))
# if num%5==0:
#     print('the number was able to divide')
# else:
#     print('number cannot divided')    

# Accept one integer value from the user; check whether entered number is between 0-100 or
# not.

# num=int(input('enter a number'))

# if 0 <= num <= 100:
#   print('number is between 0-100')
# else:
#   print('number is noot between 0-100')  

#   Accept one integer value from the user; display the length of the entered number, also display
# that the entered number is of four digits or not.

# num=int(input('enter a number'))

# length=len(str(abs(num)))
# print('the length of number is',length)

# if length==4:
#     print("the length is four ddigit")
# else:
#         print("the length is not four digit")

#         Accept one integer value from the user; display appropriate day of the week.

# day=int(input("enter a day of week"))
# if day==1:
#     print("sunday")
# elif day==2:
#     print("monday") 
# elif day==3:
#     print("tuesday")
# elif day==4:
#     print("wednesday")
# elif day==5:
#     print("thursday")
# elif day==6:
#     print("friday")
# elif day==7:
#     print("saturday")
# else:
#     print("enter valid day")    
                           
# Take choice from the user, and perform the arithmetic operation as per the choice.
# Choices: 1) Addition, 2) Subtraction, 3) Multiplication 4) Division

# print("enter your choice 1.add 2.sub 3.mul  4.div")
# choice=int(input("eneter choise between 1-4"))
# a=float(input("enter 1 number"))
# b=float(input("enter second number"))
# if choice==1:
#     print("ans",a+b)
# elif choice==2:
#     print("ans",a-b)
# elif choice==3:
#     print("ans",a*b)
# elif choice==4:
#     print("ans",a/b)
# else:
#     print("enter valid option")    
# Accept the string from the user; display the count of vowels and consonants

# s=input('enter string')
# v=c=0
# for ch in s:
#     if ch.lower() in"dnejn":
#         v += 1
#     elif ch.isalpha():
#         c+=1
# print("vowel",v)
# print("consonants",c)            

# Accept one integer value from the user; display the table of it.
# rr=int(input("enter a number"))

# for i in range(1,11):
#     print(f"{rr}*{i}={rr*i}")

#  Display square and cube of numbers 1-10.

# for i in range(1,11):
#     print(f"number:{i}, Squre:{i**2}, Cube:{i**3}")


#     Accept string from the user; convert the string to upper case.

# ab=input('enter A STRING')
# print(ab.upper())

# Display the following output using loop:
# i. 1 to 10
# ii. 10 to 1
# iii. 1 3 5 7 9
# iv. 2 4 6 8 10

# for i in range(1,11):
#     print(i,end="")


# for i in range(10,0,-1):
#     print(i,end="")    

# for i in range(1,11,2):
#     print(i,end="")

# for i in range(2,11,2):
#     print(i,end="")

# Print 1 2 4 8 16 32 64 128 256 512 1024
# num=1
# for num in range(11):
#     print(num,end="")
#     num*=2

# num=1
# for i in range(11):
#     print(num,end="")
#     num=num*2

#     Accept numbers from the user; display the sum of the entered numbers

# a=float(input("enter a number"))
# b=float(input("enter a number"))
# print("sim=",a+b)

# 15) Accept numbers from the user; display the count of the entered numbers.

# num= input("enter a number separate by space").split()  
# print("count=",len(num))

# Accept numbers from the user; find and display number of zeros available in the number
# i=input("enter number")
# print("count to zero",i.count("0"))
# ) Accept an integer from the user; tell user that whether entered number is even or odd.
# Required output:
# Enter the number: 7
# 7 is an odd number
# Do you want to check another number? Y
# Enter the number: 2
# 2 is an even number
# Do you want to check another number? N
while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

    choice = input("Do you want to check another number? (Y/N): ")
    if choice.lower() != 'y':
        break