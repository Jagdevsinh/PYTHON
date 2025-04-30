# 1). Demonstrate the use of /n and \t by printing the long string. Take input from the user.

# s = input("Enter a string: ")
# print(f"\n\t{s}\n\t")

# j=input("game ee lakho ")
# print(f"\n\t{j}\n\t")


# 2). Take one variable, store a string and display 3rd and 5th character of the string. Take input from the user.

# s=input("enter a string")
# print("third charecter of string",s[3])
# print("fifth charecter of string",s[5])


# j=input("enter string in for finding number")
# print("seventh charecter is",j[7])
# print("8th charecter is",j[8])


# 3). Take 3 numeric values in one variable, add those three values and display.

# num=input("enter any number")
# a,b,c= map(float,num.split())
# print("sum",a+b+c)

# . Perform the following calculation: a*7/b+a, where value of a=2 and b=16
# a=2
# b=16
# result=a*7/b+a
# print("result is:",result)

# j=3
# b=21
# resulte=j*7/b+j
# print("result is",resulte)

# 5). Take input from the user at command line. The values must be a number, a string and the list.

# num=float(input("enter the number"))
# str=input("enter the string")
# lst= input("enter list in comma separated").split(',')

# print('number',num)
# print('str',str)
# print('lst',lst)

# kkk=float(input('enter a number'))
# str=input('enter string')
# lst=input('enter a list').split('|')
# print(kkk)
# print(str)
# print(lst)


# aaa=float(input('enter a number'))
# ggg=input('enter a string')
# lst=input('enter a list').split(',')


# # print(f"The name of file is abc.py and its values are [{aaa}, '{ggg}', {lst}]")
# print("the name of file is abc.py and its values are[{aaa},'{ggg}',{lst}]")

# Insert string into the variable and perform following tasks:
# -Print the type of the variable with a message “The type of the variable is:”
# -Print the string with a message “The string is:”
# -Display the 3rd character of the string
# -Display character from 4th to 6th from the string
# -Change the 3rd character of the string replace it with ‘A’

# v='this is string'
# print("this is type string",type(v))

# print("the string is:",v)

# print("the third charecter of string is",v[3])
# print('the chareter from 4 to 5th is',v[4:6])

# s_modified=v[:2]+'A'+v[3:]
# print('the third charecter from string replace',s_modified)

# Store the integer value using int() class.
# -Insert an Octal value in the variable and convert it to decimal.
# -Insert the binary value in the variable and convert it to decimal.
# -Insert the float value in the variable convert it to decimal.

# x=int(25)
# print("the integer is",x)

# oct= 0o26
# print("convert octel to decimal",int(oct))

# bin= 0b11
# print('the binary is',int(bin))

# f= float(33.99)
# print('the float is',f)

# Create a list with variety of data and perform following tasks:
# -Print all the element of the string.
# -Display the class.
# -Display the first element of the list.
# -Display the 4th element of the list using negative index.
# -Change the 4th element of the list.

# list=['aaa',3434,True,90.90]
# print('list')
# print('display type',type(list))
# print('the first element',list[0])
# print('the fourth element of list',list[-1])
# list[3]="changed"
# print("change 4th element of list",list)

# list[1]="True"
# print("changed 1 charecter as",list)

# . Create a tuple using a tuple() class.
# -Modify the 1st element of the tuple.
# -Display the 3rd to 6th element from the tuple.
# -Display the 3rd to 6th element from the tuple using negative index

# mytuple=([1,2,3,4,5,6,7,8])
# print("mytuple is",mytuple)
 

# print("third charecter and sixth charecter from tuple",mytuple[2:6])

# print("third and sixth using negative",mytuple[-6:-2])

# Create a dictionary with at least 10 values and perform the following task:
# -Display all the elements of the dictionary.
# -Check the class of the dictionary you made.
# -Display the value stored in the key 7.
# -Change the value stored in the key 7.
# -Display all the values only.

# dict={
#     1:"aaa",
#     2:"bbb",
#     3:"ccc",
#     4:"ddd",
#     5:"eee",
#     6:"fff",
#     7:"ggg",
#     8:"hhh",
#     9:"iii",
#     10:"kkk"

# }

# print("display dictionary",dict)
# print("check the class",type(dict))
# print("display 7 th value",dict[6])
# dict[7]="yyy"
# print("update value",dict[7])
# print("mylist values",list(dict.values()))

# set={'aaa',True,3.5,455}

# print('this is original set',set)

# set.add("hello")
# print("this is duplicate",set)
# set.add("hellow")
# print("this is another value",set)
# set.add("555")
# print("this is another one",set)
# set.remove(1)
# set.discard("555")
# print("after removing value",set)
# set.remove(1)
# set.discard("aaa")
# print("after removing",set)


# Create a set containing varieties of value and perform following task (the set must be not modifiable):
# -Try to insert the duplicate value.
# -Add two values in the set.
# -Remove two values from the set.


# set=frozenset({'aaa',True,3.5,455})

# print('this is original set',set)
# try:
#     set.remove("hello")
# except AttributeError:
#     print("it is not changable")

# Create a bytes and perform the following tasks:
# -Display the first element using negative index.
# -Display the last element using positive index.
# -Add two values in to it.
# -Modify the last element.

# mybytes=bytes([10,20,30,40,50])
# print("this is my byte",mybytes)

# print("this is nagative index",mybytes[-len(mybytes)])
# print("this is nagative index",mybytes[len(mybytes)-1])

# try:
#     mybytes += bytes([60, 70])  
#     print("After adding values:", mybytes)
# except TypeError:
#     print("Cannot add to bytes directly")
# Create a bytes array and perform the following tasks:
# -Display the first element using negative index.
# -Display the last element using positive index.
# -Add two values in to it.
# -Modify the last element.
# -Remove the last values from the set.

# mybytes=bytearray([10,20,30,40,50])
# print("this is negative",mybytes[-len(mybytes)])    
# print("this is last element positive",mybytes[len(mybytes)-1])

# mybytes.extend([60,70])
# print("adding two values",mybytes)

# mybytes[-1]=99
# print("add two values",mybytes)

# mybytes.pop()
# print("pop the last element",mybytes)
