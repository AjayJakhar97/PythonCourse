# Python Logical Operators : are used to combine conditional statements
# ==============================

'''
and :	Returns True if both statements are true		
or	:   Returns True if one of the statements is true	x < 5 or x < 4	
not	:   Reverse the result, returns False if the result is true	not(x < 5 and x < 10)
'''

#%% 
x = 2
print(x < 5 and  x < 10)

x = 4
print(x < 5 or x < 3)

x = 2
print(not(x < 5 and x < 10))

