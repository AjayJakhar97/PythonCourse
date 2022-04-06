
#%% IndentationError

def myFunc(myList):
    for i in myList:
    # if i == 'foo':
        if i == 'foo':
            pass

myList=['foo','bar']
myFunc(myList)

#%% TabError

numbers = [3.50, 4.90, 6.60, 3.40]
def calculate_total(purchases):
    total = sum(numbers)
  return total
total_numbers = calculate_total(numbers)
print(total_numbers)
