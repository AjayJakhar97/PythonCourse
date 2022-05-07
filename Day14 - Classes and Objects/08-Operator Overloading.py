'''
Python Operator Overloading
===========================

Python Operator Overloading enables us to use mathematical, logical and bitwise operators on python objects just like any primitive data type.

For example, you can easily add two numbers 3 and 5 with + operator, i.e. 3+5 and the result is 8

But what if you want to add two circles (object of a circle class) and make a circle having twice the radius? Or 
what if you want to add two cartesian grid points to yield another point with the same '+' operator? 

Python operator overloading allows you to perform operations just like those.

'''
# %% Let's implement one in this example
'''
The correspondence between operator symbols and method names is as follows: 

x+<y calls x.__add__(y)
x–<y calls x.__sub__(y)
x*<y calls x.__mul__(y)
x/<y calls x.__truediv__(y)
x//<y calls x.__floordiv__(y)
x%<y calls x.__mod__(y)
x**<y calls x.__pow__(y)
x&<y calls x.__and__(y)
x|<y calls x.__or__(y)
x^<y calls x.__xor__(y)

'''

class GridPoint:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other):
        return GridPoint(self.x + other.x, self.y + other.y)

    def __str__(self) -> str:
        return str(self.x) + ',' + str(self.y)


point1 = GridPoint(3, 5)
point2 = GridPoint(-1, 4)
point3 = point1 + point2
print(point3)

#%% Have a look at various methods in int class and __add__ along with others can be seen there which as per documentation can be used for addition

print(dir(int))

#%% documentation for int and method __add__
'''
Reference: https://docs.python.org/3/reference/datamodel.html#object.__add__

3.3.8. Emulating numeric types
The following methods can be defined to emulate numeric objects. Methods corresponding to operations that are not supported by the particular kind of number implemented (e.g., bitwise operations for non-integral numbers) should be left undefined.

object.__add__(self, other)
object.__sub__(self, other)
object.__mul__(self, other)
object.__matmul__(self, other)
object.__truediv__(self, other)
object.__floordiv__(self, other)
object.__mod__(self, other)
object.__divmod__(self, other)
object.__pow__(self, other[, modulo])
object.__lshift__(self, other)
object.__rshift__(self, other)
object.__and__(self, other)
object.__xor__(self, other)
object.__or__(self, other)

These methods are called to implement the binary arithmetic operations (+, -, *, @, /, //, %, divmod(), pow(), **, <<, >>, &, ^, |). For instance, to evaluate the expression x + y, where x is an instance of a class that has an __add__() method, x.__add__(y) is called. The __divmod__() method should be the equivalent to using __floordiv__() and __mod__(); it should not be related to __truediv__(). Note that __pow__() should be defined to accept an optional third argument if the ternary version of the built-in pow() function is to be supported.

If one of those methods does not support the operation with the supplied arguments, it should return NotImplemented.

'''
# %% similary, let's try overloading Relational Operators
'''
The correspondence between operator symbols and method names is as follows: 
x<y calls x.__lt__(y), 
x<=y calls x.__le__(y), 
x==y calls x.__eq__(y), 
x!=y calls x.__ne__(y), 
x>y calls x.__gt__(y), and 
x>=y calls x.__ge__(y)

'''
class GridPoint:  
    def __init__(self, x, y):  
        self.x = x  
        self.y = y  
  
    def __gt__(self, other):  # Overloading the greater than operator
        return self.x > other.x  
# Returns true if value of x in the left operand is greater than that in the right one. Returns false otherwise
  
    def __str__(self):  
        string = str(self.x)  
        string = string + ", " + str(self.y)  
        return string  
  
point1 = GridPoint(3, 5)  
point2 = GridPoint(-1, 4)  
if point1 > point2:  # Compares with the overloaded __gt__() method
    print('point1 is greater than point2')  
else:  
    print('point1 is not greater than point2')

