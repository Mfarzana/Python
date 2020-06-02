import random
# solution for 1 times
secret_num=random.randint(0,20);
user_input=int(input("Enter number: "))
if secret_num > user_input:
    print("too hight")
elif secret_num == user_input:
    print("hit")
else:print("too low")

#solution 2

secret_num=random.randint(0,3);

while True:
    try:
        user_input=int(input("Enter Number: "))
        if user_input > secret_num:
            print("too high")
        elif user_input < secret_num:
            print("too low")
        else:print("hit")

    except ValueError:
        print("Please input a valid Number")
