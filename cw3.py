# #Write a program to check whether two entered numbers are equal or not
#num1=int(input("enter a first no:"))
#num2=int(input("enter second no"))
#if(num1==num2):
 #   print("it is equal")
#else:
 #   print("it is not equal")


# #Write a program to check whether two entered words are equal or not
#word1=str(input("enter first word"))

#word2=str(input("enter second word"))
#if(word1==word2):
 #   print("it is equal")
#else:
 #   print("it is not equal")
# #Write a program to find the maximum of two numbers
#a=int(input("enter first no"))
#b=int(input("enter second no"))
#if(a>b):
 #   print("a")
#else:
 #   print("b")



# #write a program to check whether the entered character is vowel or not
#char=input("enter a character")
#vowels='aeiouAEIOU'
#if(char in vowels):
 #   print("it is vowels")
#else:
 #   print("it is not vowels")
# #Write a program to check whether the entered country name contains word 'land'
#a=input("enter a string")
#if('land' in a):
 #   print(a)
#else:
 #   print("it is not")
# #write a program to check whether the entered number is 3 digit or not
#a=int(input("enter a no:"))
#if(99<=a<=999):
 #   print(a)
#else:
#    print("not")

#write a program to check whether the entered string is  palindromde or not
#b=input("enter a string:")
#if[b==b[::-1]]:
 #   print("it is palindrome")
#else:
 #   print("it is not palindrome")

    #Write a program to check whether a number is present in given list
#l=[23,67,12,90]
#a=int(input("enter a no:"))
#if(a in l):
 #   print("it is present")
#else:
 #   print("it is not present")

#Write a program to check whether a key is prsent in a dictionary or not
#d={101:'Arun',102:'Amal',103:'Anu'}
#b=int(input("enter a no"))
#if(b in d):
 #   print(b)
#else:
 #   print("not present")

#Write a program to check whether the given pasword is strong/weak(if length lessthan 8 weak)
#a=input("enter a password")
#if(len(a)>=8):
 #   print("strong")
#else:
 #   print("not strong")


 #if elif

#a=int(input("enter first no:"))
#b=int(input("enter second no:"))
#c=int(input("enter third no:"))
#d=int(input("enter forth no:"))
#if(a>b and a>c and a>d):
 #    print("large is a")
#elif(b>c and b>a and b>d):

 #   print("b is large")
#elif(c>a and c>b and c>d):

#write a program to check whether an entered no is 2digit/3 digit/4 digit
a=int(input("enter a no:"))
if(9<a<99):
    print("a is 2 digit no")
elif(99<999):
    print("a is 3 digit no")
elif(999<9999):
    print("a is 4 digit no")
else:
    print("it is invalid")

#writ a basic calculator prgm to perform arithemetic oprts

a=int(input("enter a no:"))
b=int(input("enter a no:"))
opr=input("enter a opr:")
if(op=='+'):
    print("sum is",a+b)
elif(op=='-'):
    print("diff is",a-b)
elif(op=='*'):
    print("mul is",a*b)
elif(op=='/'):
    print("div is",a/b)
else:
    print("invalid")