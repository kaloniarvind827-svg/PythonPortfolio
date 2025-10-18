num1=int(input("Enter first number"))
num2=int(input("Enter second number"))
num3=int(input("Enter third number"))

print(f'{num1} is greatest') if num1>num2  and num1>num3 else( print(f'{num2} is greatest') if num2>num3 else print(f'{num3} is greatest'))


print(f'{num1} is smallest' if num1<num2 and num1<num3 else(print(f'{num2} is smallest')if num2<num3 else print(f'{num3} is smallest')))

print("all are equal") if num1==num2==num3 else print("all are not equal")