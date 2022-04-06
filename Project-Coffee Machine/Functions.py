from time import sleep

OrderList = []
OrderHistory = []

def Logo():
    print('''

___________.__             _________         _____       
\__    ___/|  |__   ____   \_   ___ \_____ _/ ____\____  
  |    |   |  |  \_/ __ \  /    \  \/\__  \\   __\/ __ \ 
  |    |   |   Y  \  ___/  \     \____/ __ \|  | \  ___/ 
  |____|   |___|  /\___  >  \______  (____  /__|  \___  >
                \/     \/          \/     \/          \/ 

''')

def Tea():
    print("You have ordered tea")
    OrderList.append("Tea")
    WelcomeScreen()

def Chocolate():
    print("You have ordered chocolate")
    OrderList.append("Chocolate")
    WelcomeScreen()

def HotChocolate():
    print("You have ordered hot chocolate")
    OrderList.append("Hot Chocolate")
    WelcomeScreen()

def Coffee():
    print("You have ordered coffee")
    OrderList.append("Coffee")
    WelcomeScreen()

def WelcomeScreen():
    Logo()
    print("Welcome to the Coffee Maker!")
    print("What would you like to order?")
    print("1. Coffee")
    print("2. Tea")
    print("3. Hot Chocolate")
    print("4. I don't want to order anything")
    print("5. I want to see my order")
    print("6. I want to see my order history")
    print("7. I want to see my order history and order again")

    order = int(input("Please enter your choice: "))
    if order == 1:
        Coffee()
    elif order == 2:
        Tea()
    elif order == 3:
        HotChocolate()
    elif order == 4:
        print("Thank you for your order!")
    elif order == 5:
        print("Your order is: " + str(OrderList))
        uniqueItemLists = set(OrderList)
        print(uniqueItemLists)
        for item in uniqueItemLists:
            count = OrderList.count(item)
            print(item + ": " + str(count))

    elif order == 6:
        print("Your order history is: " + str(OrderHistory))
    elif order == 7:
        print("Your order history is: " + str(OrderHistory))
        WelcomeScreen()
    else:
        print("Please enter a valid choice")
        WelcomeScreen()
