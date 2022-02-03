# %% Task 01 - Create a program to test if number is 0,+ve or -ve

number = input("Enter your number: ")
try:
    int(number)
    if number > 0:
        print("+ve")
    elif number == 0:
        print("zero")
    elif number < 0:
        print("-ve")
except:
    print("Invalid Input")

