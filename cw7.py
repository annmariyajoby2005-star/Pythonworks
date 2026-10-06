# # # Q1.Define a function that takes 2 numbers and returns their product
# def product(a,b):
#     return a*b
# print(product(7,8))


#
# # Q2.Define a function that takes a string and returns number of vowels
# def vowels(a):
#     count=0
#     for i in  a:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count
# print(vowels("Annmariya"))




#
# # Q3.Define a function that takes length and breadth and returns area of
# #rectangle
# def area(l,b):
#     a=l*b
#     return a
# l=int(input("Enter length:"))
# b=int(input("Enter breadth:"))
# result=area(l,b)
# print(result)

#
# # Q4.Define a function that takes a list of numbers and creates a new list
# # # with even numbers and returns the new list
# l=[45,78,90,12,35]
# def even(lst):
#     new=[]
#     for i in lst:
#         if i%2==0:
#             new.append(i)
#     return(new)
# print(even(l))



# #Q5.Define a function that takes list of 3 digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.
# l = [123, 345, 111, 678, 134, 809]

# new=[6,12,3,21,8,17]
# def smlst(l):
#     new=[]
#     for i in l:
#         sum=0
#         for j in str(i):
#             sum=sum+int(j)
#         new.append(sum)
#     return new
# result=smlst(l)
# print(result)
#define a function that takes a list of arguments and returns a new list containing uniq elements from the list
# l=[12,34,78,12,67,34,90,23]
# def lst(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
# result=lst(l)
# print(result)
#define a function that takes 2 list as arguments and print common elements
# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def common(list1,list2):
#     new=[]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#     return new
# new=common(list1,list2)
# print(new)
#or...........................

# def common(list1,list2):
#     for i in list1:
#         if i in list2:
#             print(i)
#     return
# common(list1,list2)
# def fun(n,a):
#     print("Name",n)
#     print("Age",23)
# # fun(n="arun",a=23)
#args
# fun(a=23,n="arun")
# def fun(*args):
#     print(args)
# fun(2,45)
# fun(34,67,89,23,90)
# fun(8888,9999,6)
#kwargs
# def fun(**kwargs):
#     print(kwargs)
# fun(name="Aaaa",age=23)
# fun(name="Maya",age=23)
# fun(name="aaOO")
#define a function that accepts any no of returns their sum
# def fun(*args):
#     sum=0
#     print(args)
#     for i in args:
#         sum+=i
#     return sum
# print(fun(23,56))









# # # #Write a program to find the position of a character in a string
# k=input("Enter a string")
# p=input("Enter the character")
# print(k.find(p))


# # # #write a program to find the count of character in  a string
# a=input("Enter a string")
# n=input("Enter a character")
# print(a.count(n))
# # #create a random 5 digit otp number and print otp number
# import random
# a=random.randint(100000,999999)
# print("OTP",a)

# #create a list of  5 random 3 digit numbers
# import random
# a=[]
# for i in range(1,6):
#     otp=random.randint(100,999)
#     a.append(otp)
# print(a)



# #create a dictionary where keys are words and values are length of each word from the string




# #new={'python':6,'coding':6,'is':2,'easy':4,'and':3,'fun':3}
# s="python coding is easy and fun"
# new={}
# for i in s.split():
#     new[i]=len(i)
# print(new)
# #create a dictionary where keys are each character and values are number of occurence of each character


#d={'h':1,'e':1,'l':3,'o':2,'':1,'w':1,'r':1,'d":1'}
# s="hello world"
# new={i:s.count(i)for i in s}
# print(new)

# #write a program to find the number of digits,letters,and spaces in a string

# s="sdfghjk3456789  dffghjkl345678"
# letters=0
# digit=0
# space=0
# for i in s:
#     if i.isalpha():
#         letters=letters+1
#     if i.isdigit():
#         digit=digit+1
#     if i.isspace():
#         space=space+1
# print("Letters",letters)
# print("Digits",digit)
# print("Space",space)

# # Given a list
# l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# new=[i[2]for i in l]
# print(new)

# # # create a list of salaries


# # # find the maximum salary
# new=[i[2]for i in l]
# print(max(new))
# # # find minimum salary


# new=[i[2]for i in l]
# print(min(new))
#Given a dictionary
d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}

# create a new list of students whose mark>=40
new={}

#Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# Find Common elements


#Given l=23,45,67,12,90,56]
#find second largest number

#find second smallest number
#union,intersection
#Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# #Given two lists
# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))
#compaine two list without duplicates
# s1=set(l1)
# s2=set(l2)
# print(s1.union(s2))

d={'a':10,'b':20}
for i,j in d.items():
    print(i,j)
