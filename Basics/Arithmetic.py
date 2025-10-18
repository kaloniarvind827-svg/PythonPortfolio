num1 = int(input("Enter 1st number"))
num2 = int(input("Enter 2nd number"))


print(f'sum of the numbers is : {num1+num2}')
print(f'difference of the numbers is : {(num1-num2) if num1>num2 else (num2-num1)}')
print(f'product of the numbers is : {num1*num2}')
print(f'division of the numbers is : {num1/num2}')

if(num1+num2>100):
    print("Wow! That's a big number")