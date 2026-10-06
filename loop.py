#loop
#i=10
#while(i<=20):
 #   print(i)
  #  i=i+1


#1,3,5,7,9,11
#i=1
#while(i<=11):
 #   print(i)
  #  i=i+2




#while


# # #1,2,3,4,5,.....100
#i=1
#while(i<=100):
   # print(i)
    #i=i+1

# # #1,3,5,7,9,11,13,15
#i=1
#while(i<=15):
 #   print(i)
  #  i=i+2

# #2,4,6,8,10,12
#i=2
#while(i<=12):
 #   print(i)
  #  i=i+2

# #1,4,7,10,13,16

#i=1
#while(i<=16):
 #   print(i)
  #  i=i+3

#10,20,30,40,50,60,70,80
#i=10
#while(i<=80):
 #   print(i)
  #  i=i+10


#3,6,9,12,15,18,21
#i=3
#while(i<=21):
 #   print(i)
  #  i=i+3

#5,4,3,2,1
#i=5
#while(i>=1):
 #   print(i)
  #  i=i-1

#8,6,4,2,0
#i=8
#while(i>=0):
 #   print(i)
  #  i=i-2

#100,101,102,.....200
#i=100
#while(i<=200):
#    print(i)
 #   i=i+1


#print all 4 digit numbers(1000-9999)
# i=1000
# while(i<=9999):
#     print(i)
#     i=i+1

##print those 3 digit numbers that are divisible by 3
# i=100
# while(i<=999):
#     if(i%3==0):
#      print(i)
#     i=i+1

#print those 4 digit no that contains '3'

# i=1000
# while(i<=9999):
#     s=str(i)
#     if('3'in s):
#         print(i)
#     i=int(i)+1

#print those no that are divisible by 3 and 5 range(1,100)

# i=1
# while(i<=100):
#     if(i%3==0 and i%5==0):
#         print(i)

#1,4,9,16,25,36,49,64,81,100
# i=1
# while(i<=10):
#
#     print(i,i*i)
#     i=i+1

#count of those 3 digit no that contains digit 3
# count=0
# i=100
# while(i<=999):
#     if('3'in str(i)):
#         print(i)
#         count=count+1
#     i=i+1

#count those no that are divisible by 7 or 3 in the range (200,300)
# i=200
# while(i<=300):
#     if(i%7==0 and i%3==0):
#         print(i)
#     i=i+1
#count of odd no that are divisible by 5 in the range (1,100)

#
# l=[12,4.5,6.8,30,"arun","hello"]
# float point values
# for i in l:
#     if(type(i)==float):
#         print(i)
# #string valuess
# for i in l:
#     if(type(i)==str):
#         print(i)
#Numbers
# for i in l:
#     if(type(i)==int or type(i)==float):
#         print(i)
# #dictonary
# d={'a':23,'b':25,'c':28,'d':30,'e':22}
# #even values
# for i in d.values():
#     if(i%2==0):
#         print(i)

# colors=['red','green','blue','orange','black']
# # #starting letters
# # for i in colors:
# #     print(i[0])
#
# #last letter
# for i in colors:
#     print(i[-1])
#reverse
# for i in colors:
#     print(i[::-1])
#all clrs contains letter 'b'
# for i in colors:
#     if('b'in i):
#         print(i)


#range
#Range

# 1,2,3,4,5
# for i in range(1,6):
#     print(i)

#1,3,5,7,9,11
# for i in range(1,12,2):
#     print(i)
#2,4,6,8,10
# for i in range(2,11,2):
#     print(i)
#100,200,300,400,500
# for i in range(100,600,100):
#     print(i)
#5,4,3,2,1
# for i in range(5,0,-1):
#     print(i)

#3,6,9,12,15,18,21
# for i in range(3,22,3):
#     print(i)
# #1,4,9,16,25,36
# for i in range(1,7):
#     print(i*i)

#print all 3 digit numbers(100-999)

# for i in range(100,1000):
#     print(i)

#print all numbers divisible by 3 in the range 100-200
# for i in range(100,201):
#         if(i%3==0):
#             print(i)
#1,8,27,64,125
# for i in range(1,6):
#     print(i*i*i)

#print each no in a list
l=[12,12,343,78]
#
# for in l:
#     print(i)

#print each no in digit
# n=1234
# s=str(n)
# for i in s:
#     print(i)

#sum of a list
#n=[1,2,3,4]
# sum=0
# for i in n:
#     sum=sum+1
# print(sum)

#sum of digits in a no
# n=1234
# sum=0
# s=str(n)
# for i in s:
#     sum=sum+int(i)
# print(sum)

#reverse of a string without using slice
# s="hello"
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

#reverse of a no
# n=1234
# s=str(n)
# rev=""
# for i in s:
#     rev=i+rev
# print(rev)

#given a list
l=[1,2,3,4]
# print square of each no
# for i in l:
#     print(i**2)
#create a new list with squares of each elements
# new=[]
# for i in l:
#     new.append(i**2)
# print(new)
#create a new set
# new=set()
# for i in l:
#     new.add(i)
# print(new)
#create a new dictionary where keys are no and values are square of
#d={1:1,2:4,3:9,4:16}
# new={}
# for i in l:
#     new[i]=i**2
# print(new)
#break

# s="hello"
# for i in s:
#     if(i=='l'):
#         break
#     print(i)

#continue
# for i in s:
#     if(i=='l'):
#         continue
#     print(i)
#Given a list
colors=['red','green','blue','yellow','black','orange']
# #print each color
# for i in colors:
#     print(i)
# #print the first color starting with 'b'
# for i in colors:
#     if(i[0]=="b"):
#         print(i)
#         break

#print all colors except color starting with 'b'
# for i in colors:
#      if(i[0]=="b"):
#         print(i)
#         continue

#print the first color contains letter 'n'
# for i in colors:
#       if(i=="n"):
#        print(i)



# #print all colors except color contains letter 'n'
# for i in colors:
#      if(i=="n"):
#          print(i)
#          break

