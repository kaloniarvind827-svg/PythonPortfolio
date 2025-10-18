user_name = input("Enter your name : ")
user_age = int(input("Enter your age : "))

print(f'Hello {user_name}! How are you? You will be  {user_age+1} year old next year')

if(user_age>=13 and user_age<=19):
    print("you are a teenager ")
else:
    print("you are not a teenager ") 