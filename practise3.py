# Get the basic salary from the employee and display the net salary by calculating the following
# conditions: Applicable TA 4%, DA 30%, HRA 15% on basic salary. Applicable 3% tax, 12% PF on
# basic salary.
# basic=float(input("enter basic salary"))

# ta=0.04*basic
# da=0.30*basic
# hra=0.15*basic

# tax=0.03*basic
# pf=0.12*basic

# netsal=ta+da+hra-tax-pf
# print("net salary",netsal)

# Get the marks of 5 subjects at the command line and display the total of marks, and percentage.
# mark1=float(input('enter subject mark'))
# mark2=float(input('enter subject mark'))
# mark3=float(input('enter subject mark'))
# mark4=float(input('enter subject mark'))
# mark5=float(input('enter subject mark'))

# total=mark1+mark2+mark3+mark4+mark5
# percent=(total/500)*100
# print("total marks",total)
# print("total percent",percent,"%")

# Rajkot Corporation wants to make simple application to calculate Water Bill of Rajkotians. Water
# is being delivered by the Corporation on per litre charges as below:
# Upto 90 litres – Rs. 0/ltr
# Upto 150 litres – Rs. 2/ltr
# Upto 250 litres – Rs. 5/ltr
# More than 250 – Rs. 10/ltr
# Accept unit consumption from consumer and display the bill amount.

# litres=int(input("enter water consuption in literes"))
# bill=0

# if litres <=90:
#  bill=0
# elif litres <=150:
#  bill =(litres-90)*2 
# elif litres <=250:
#  bill =(60*2)+(litres-150)*5
# else:  
#  bill=(60*2)+(100*5)+(litres-250)*100

#  print("water bill amount is",bill)
#  A tuition class owner wants to make a simple application to allocate grade to the students on
# the basis of marks student have scored. Accept marks from the students.
# Marks more than 90 – A1 grade
# Marks 80 or less than or equal 90 – A grade
# Marks 70 or less than or equal 80 – B1
# Marks 60 or less than or equal 70 – B
# Marks 50 or less than or equal 60 – Can do Better!
# Marks <50 – Need to work hard.

# marks=float(input("enter your marks"))

# if marks>90:
#     grade="A1"
# elif marks>80:
#     grade="b1"
# elif marks>70:
#     grade="b"
# elif marks>60:
#     grade="can do better" 
# else:
#     grade="need to work hard."

# print("your grade",grade)                  

# Income Tax department wants to make an application that calculates tax on the basis of the
# income. Accept yearly income earned by the taxpayer as an input and calculate tax to be paid.
# The tax slab is as below:
# Income up to 8 lakhs – No tax
# Income more than 8 lakh and less than 10 lakhs – 15% of income
# Income more than 10 lakhs and less than 20 lakhs – 20% of income
# Income more than 20 lakhs – 30% of income


# income=float(input("enter your yearly income"))

# if income <=80000:
#     tax=0
# elif income<=100000:
#     tax=income*0.15
# elif income<=200000:
#     tax=income*0.20
# else:
#     tax=income*0.30

# print("enter income tax",tax)

#  Accept two integer values in separate variable, display the small value and big value out of it.
# a=int(input("enter first"))
# b=int(input("enter second"))
# print("smaller",min(a,b))
# print("bigger",max(a,b))

# Accept marks from 4 students, display which mark is highest among all.
# student1=int(input("enter marks"))
# student2=int(input("enter marks"))
# student3=int(input("enter marks"))
# student4=int(input("enter marks"))
# print("highest",max(student1,student2,student3,student4))


amount = float(input("Enter your shopping amount: "))
if amount < 1500:
    shipping = 100
    print("Please purchase Rs.", 1500 - amount, "more to avail shipping charge of Rs. 80/-")
    print("Please pay Rs.", amount + shipping)

elif amount < 3000:
    shipping = 70
    print("Please purchase Rs.", 3000 - amount, "more to avail shipping charge of Rs. 50/-")
    print("Please pay Rs.", amount + shipping)

else:
    discount = amount * 0.07
    final_amount = amount - discount
    print("You saved Rs.", discount)
    print("Please pay Rs.", final_amount)
