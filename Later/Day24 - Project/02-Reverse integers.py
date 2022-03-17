# %% Reverse a whole number
'''
input  : 23597
output : 79532

input  : 1
output : 1

input  : 10000
output : 1

input  : 123456
output : 654321

'''


def ReverseInt(myInteger):
    result = 0
    while(myInteger > 0):
        result = result * 10 + int(myInteger % 10)
        myInteger = int(myInteger/ 10)
    return result

print(ReverseInt(23597))
print(ReverseInt(1))
print(ReverseInt(0))
print(ReverseInt(10000))
print(ReverseInt(123456))
# %%
