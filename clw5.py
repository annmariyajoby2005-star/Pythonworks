# # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print(i)

# # 2.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
# l=[4,5,6,7]
# result=[]
# total=0
# for i in l:
#     total=total+i
#     result.append(total)
# print(result)


# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25
# a=3
# b=7
# total=0
# for i in range(a,b+1):
#     total=total+i
# print(total)


# 4.Given a list, sum only the elements at even indices.
# Example:
#  → Sum = 10 + 30 + 50 = 90
# l=[10,20,30,40,50]
# total=0
# for i in range(len(l)):
#     if i%2==0:
#         total=total+l[i]
# print(total)


#5.Given a list, sum the elements until a 0 is encountered (stop at 0).
# l=[4,9,1,0,6,7]
# total=0
# for i in l:
#     if i==0:
#         break
#     total=total+i
# print(total)

# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
# for i in range(1,1000):
#     if i%7==0 and i%11==0:
#         print(i)
#         break

# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
# l=["hi","orang","hey","grapes","strawberry"]
# for i in l:
#     if len(i)<5:
#         continue
#     print(i)



# 8.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]
# l=[1,2,3]
# result=[]
# for i in l:
#     result.append(i*i)
# print(result)


# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"
# s="hello world"
# result=" "
# for i in s:
#     if i.lower() in "aeiou":
#        continue
#     result = result+i
# print(result)


#
# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number
# is greater than 50 (use break).
# l=[5,2,8,6,2]
# result=[]
# for i in l:
#     d=i*2
#     if d>50:
#         break
#     result.append(d)
# print(result)





# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"
# a="abc123x7z"
# result=" "
# for i in a:
#     if i.isdigit():
#         result=result+i
# print(result)

# 12.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]
# s=["cat","banana",""]
# result=[]
# for i in s:
#     result.append(len(i))
# print(result)

# 13.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"
# l=["Python","Is","Great"]
# result=""
# for i in l:
#     result=result+i[0]
# print(result)



# 14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
# n=[4, -3, 2, -1]
# result=[]
# for i in n:
#     if i<0:
#         result.append(0)
#     else:
#         result.append(i)
# print(result)

# 15.
# d={101:['Arun',23,'ekm'],
#      102:['Amal',25,'tvm'],
#      103:['Anu',26,'tcr'],
#       104:['Kiran',27,'ekm']}
#
# #print all names of students
# for i in d:
#     print(d[i][0])
#
# 16.Write a program to print the numbers from 1 to 100.
# But for multiples of:

# 3, print “Fizz” instead of the number

#
# 5, print “Buzz” instead of the number
#
# Both 3 and 5, print “FizzBuzz”
#
# Otherwise, print the number itself

#
# Output format example:
# 1, 2, Fizz, 4, Buzz, … , FizzBuzz, …
# for i in range(1,100):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i)
#
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue
#     Stop the loop if the number becomes greater than 40 using break
# for i in range(1,51):
#     if i>40:
#         break
#     if i%5==0:
#         continue
#     print(i)
#
# 18.Write a program to find
#     Reverse of a number(without[::-1])
#     count the number of digits in a given number
#     sum of digits in  a number
# n=int(input("enter a no:"))
# temp=n
# reverse=0
# count=0
# total=0
# while temp>0:
#     digit=temp%10
#     reverse=reverse*10+digit
#     total=total+digit
#     count=count+1
#     temp=temp//10
# print("Reverse=",reverse)
# print("count",count)
# print("sum of digits",total)

#pattern printing
#1
#4 9
#16 25 36
#49 64 81 100
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k**2,end=" ")
#         k=k+1
#     print()
#1
#333
#5555
# for i in range(1,6,2):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()

#1
#1A1
#1A1A1
#
# for i in range(1,6,2):
#     for j in range(1,i+1):
#         if j%2==0:
#             print('A',end=" ")
#         else:
#             print('1',end=" ")
#     print()
#     *
#   *  *
#  * * *
#* * * *

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(" ",end="")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end="    ")
#     print()
#     5
#   5   5
#  5  5  5
#5  5  5  5  5
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(" ",end="")
#     k=k-2
#     for j in range(1,i+1):
#         print('5',end="    ")
#     print()


#* * * *
# * * *
# #  * *
# #   *
# k=0
# for i in range(4,0,-1):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k+2
#     for j in range(1,i+1):
#         print("*",end='   ')
#     print()

# l=[1,2,3,4]
# new_list=[i**2 for i in l]
# print(new_list)
# new=[5 for i in l]
# print(new)
#given a new list
# l=[12,45,34,67,90]
#create a new list with even values
# new_list=[i for i in l if i%2==0]
# print(new_list)


#create a new list with values greater than 50
# new_list=[i for i in l if i>50]
# print(new_list)
#given a list
# color=['red','green','blue','orange']

#create a new list with first letter  of each color
# new=[i[0]for i in color]
# print(new)
#create a new list with length of each color
# new=[len(i) for i in color]
# # print(new)
#
# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# for i in range(1,5):
#         print("*"*i)
# for i in range(3,0,-1):
#        print("*"*i)
#or
# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()
# for k in range(3,0,-1):
#     for j in range(1,k+1):
#         print("*",end=" ")
#     print()

#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
# k=6
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(" ",end="")
#     for j in range(i):
#         print('*',end=" ")
#     print()
#     k=k-1
# k=4
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(" ",end="")
#     for j in range(i):
#         print('*',end=" ")
#     print()
#     k=k+1
#     **
#     **
#   ****
#   ****
#  ******
#  ******
#  ********
#  ********
# k=6
# for i in range(1,5):
#     for j in range(k):
#         print(" ",end="")
#     for j in range(i*2):
#         print("*",end=" ")
#     print()
#     for j in range(k):
#         print(" ",end="")
#     for j in range(i*2):
#         print('*',end=" ")
#     print()
#     k=k-2
# #or
# k=6
# for i in range(2,9,2):
#     for j in range(2):
#         for l in range(1,k+1):
#             print("",end=" ")
#         for q in range(1,i+1):
#             print('*',end=" ")
#         print()
#     k=k-2

# # #create a new list with square root of each element
# l=[25,16,9,36]
# new=[i**0.5 for i in l]
# print(new)

# #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # create a list of names
# new=[i for i in d]
# print(new)
# # create a list of marks
# new=[i for i in d.values()]
# print(new)
#
# #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']

# #create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)
# # #create a list of floats
# new=[i for i in l if type(i)==float]
# print(new)
# #create a list of positive numbers
# new=[i for i in l if type(i)!=str and i>0]
# print(new)

#
#
# #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# #create a new list with elements whose length is greater than 6
# new=[i for i in fruits if len(i)>6]
# print(new)

# #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1,101)if i%3==0]
# print(new)

# Given
# s="python coding  is easy and fun"
# # create a new list with only vowels
# k='a,e,i,o,u,A,E,I,O,U'
# new=[i for i in s if i in k]
# print(new)
# s="python coding is easy and fun"
# new={i for i in s if i!=" "}
# print(new)
#create a new set with only vowels
# new={i for i in s if i in "aeiouAEIOU"}
# print(new)
# new={len(i) for i in s.split()}
# print(new)
#dic comprohension
# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)
# l=[10,20,30,40]
# #create a new dictionary where keys are index of each no and values are no from not list
# new={i:l[i] for i in range(0,len(l))}
# print(new)

#given a string
s="python coding is easy and fun"
# #create a new dictionary where keys and values are length of each word
new={i:len(i) for i in s.split()}
print(new)












