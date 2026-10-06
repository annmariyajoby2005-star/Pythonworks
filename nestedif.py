#check whether a no is positive even/positive odd/negative even/negative odd
#a=int(input("enter a no:"))
#if(a>0):
 #   if(a%2==0):
 #       print("positive even")
  #  else:
   #     print("positive odd")
#else:
 #   if(a%2==0):
  #      print("negative even")
   # else:
       # print("negative odd")

#check whether a no is
#divisible by 2 and 3
#divisible by 2 and not by 3
#divisible by 3 and not by 2
#not divisible by 2 and 3

a=int(input("enter a no:"))
if(a%2==0):
    print("divisible bby 2")
    if( a%3==0):
         print("it is  divisible  3")
    else:
            print("it is not divisible by 3")
else:
    print("not divisiblr by 3")
    if(a%3==0):
        print("it is not divisible  2")
    else:
        print("not divisible by 2 ")