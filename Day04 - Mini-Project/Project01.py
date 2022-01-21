
#%% Create a program which keeps asking for input until we don't want to anymore
answer = 'Y'
while answer == 'Y' or answer == 'y' or answer == 'yes' or answer == 'YES' or answer == 'Yes':
    print("What do you want to say?")
    answer1 = input()
    print('You said, "', answer1, '"')
    answer = input("Do you want to continue? type (Y)es or (N)o ")

print("You exited the game...")
