#to print factorialof a number 
def factorial(num):
    fact=1
    for i in range(2,num+1):
        fact = fact*i
    return fact

#check prime or not without using functions

# num = int(input("Enter number to check for prime"))
# flag= None    
# for i in range(2,num**0.5+1):
#     if(num%i!=0):
#         flag=False
#         continue
#     else:
#         flag=True
#         break
# if(flag):     
#     print("it is not Prime")
# elif(flag==False):     #why not the same shortcut as above?
#     print("it is Prime")
# else:
#     print("neither prime nor composite")



    
 # This works, but it keeps overwriting flag = False for every number that does not divide num.
# Only the first divisor is important; after that, flag = True and you break.
# A better way: only mark flag = True if a divisor is found, do not set flag = False inside the loop.
# elif flag == False vs elif not flag
# not flag is the Pythonic shortcut for flag == False.
# The reason elif not flag may fail here: the flag started as None, not False.
# not None → True
# So elif not flag: would incorrectly catch numbers like 0 or 1.
# That’s why the code uses flag == False to be explicit.



# check this also
    # if(num%i==0):
    #     flag=True
    #     break 
    # else:
    #     flag=False
    #     continue



# Program 2
num = int(input("Enter number to check for prime : "))
# negative numbers are not considered for prime or composite
if(num<=1):
        print("Niether prime nor composite")
else:
    for i in range(2,int(num**0.5)+1):
        if(num%i==0):
            print("it is not Prime")
            break       
    else:     
        print("it is Prime")
       

# reverse of a given number (e.g., 1234 → 4321).
# this will not work with floating points

def reverseNum(num):
    newNum=0
    while(num>0):
        digit = num%10
        newNum=newNum*10+digit
        num=num//10
    return newNum    
print(reverseNum(12734))


def reverse_Num(num):
    return float(str(num)[::-1])
               
print(reverse_Num(124.5))            


#hcf of two numbers 

def hcf(x,y):
    small=x if x<y else  y
    grt = x if x>y else y
    ans=1
    num=2
    
    while(small>1):
        if(grt%small==0):
            ans=small
            break
        else:
            while(num<int(small**1/2+1)):
                if(small%num==0):
                    small=small%num
                else:
                    num
    return ans  

print(hcf(20,15))      
    