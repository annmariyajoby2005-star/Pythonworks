#Check whether a number is an Armstrong number
# a=int(input("enter a no:"))
# total=0
# for i in str(a):
#     total=total+int(i)**len(str(a))
# print(total)
# if total==a:
#     print("Armstrong")
# else:
#     print("not Armstrong")

#Given a list
#l=[1,2,3,4]
# create a new list with squares of each element
# new=[]
# for i in l:
#         new.append(i**2)
# print(new)


#Given a list
# l=[12,67,59,23]
#create a list with elements whose value is greater than 50.
# new=[]
# for i in l:
#   if i>50:
#     new.append(i)
# print(new)
# create a new set with elements whose value is greater than 50
# new=set()
# for i in l:
#     if i>50:
#         new.add(i)
# print(new)

#Given a list
# l=[1,2,3,4]
#create a new dictionary where keys are numbers and values are squares of each number
# d={1:1,2:4,3:9,4:16}
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

##create a list of 5 random numbers
# l=[]
# for i in range(5):
#     a=int(input("enter a no:"))
#     l.append(a)
# print(l)
#Find the factors of a number
# a=int(input("enter a no:"))
# for i in range(1,a+1):
#     if a%i==0:
#         print(i)
#find the fibinocci series
# s=int(input("enter a no:"))          or
# a=0                               a=0
# b=1                               b=1
# for i in range(s):                for i in range(1,11)
#     print(a,end="")               print(a)
#     c=a+b                         a,b=b,a+b
#     a=b
#     b=c

# for i in range(1,11):
#     if(1==5):
#          break
#     print(i)
# else:
#     print("hello")

# i=1
# while(i<=5):
#     print(i)
#     i=i+1
# else:
#     print("hello")

#write a program to check a no is prime or not
# num=int(input("enter a no:"))
# for i in range(2,num):
#     if(num%i==0):
#         print("not prime")
#         break
# else:
#     print("prime")

#check whether a no is perfect
# num=int(input("enter a no:"))
# sum=0
# for i in range(1,num):
#     if(num%i==0):
#         sum=sum+i
# if sum==num:
#         print("perfect no")
# else:
#     print("not perfect")

# for i in range(1,4):
#     for j in range(1,6):
#         print(i,j)

# l=["kelly","emy","alan"]
# for i in l:
#     for j in range(1,4):
#         print(i)

# no=[1,2,3]
# qns=["what","when","why"]
# for i in no:
#     print(i,'.')
#     for j in qns:
#         print(' ',j)

# l=[[1,2,3][5,6,7,8]]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)

# d=[{'id':101,'name':'arun','age':23},
#     {'id':102,'name':'amal','age':24},
#     {'id':103,'name':'anu','age':22}]
#
# for i in d:
#     print(i)
#     for j in i.values():
#         print(j)

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=" ")
#     print()
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#1 0 0 0
#0 1 0 0
#0 0 1 0
#0 0 0 1
# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()
#1
#2 3
#4 5 6 7
#8 9 10 11
# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+1
#     print()
#2
#4 6
#8 10 12
k=2
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+2
#     print()
# * * * *
# * * *
# * *
# # *
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
#55555
#4444
#333
#22
#1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()
#1
#2 1
#3 2 1
#4 3 2 1
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j,end=" ")
#     print()
#1
#1 0
#1 0 1
#1 0 1 0
# for i in range(1,5):
#     for j in range(1,i==):
#         if i:
#             print(1,end=" ")
#         else:
#             print(0,end=" ")
#     print()

#A
#B B
#C C C
#D D D D
# k=65
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#     k=k+1
#     print()
#A
#A B
#A B C
#A B C D
# for i in range(1,5):
#     k=65
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()
#l=[12,34,56,78,13,87,5]
# #print all prime no on the given list
# for i in l:
#     for j in range(2,i):
#          if i%j==0:
#             break
#     else:
#         print(i)
#print all prime no in the range(1,100)
# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


