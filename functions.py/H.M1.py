#Q1 Take two arguments and return their sum
def add(a, b):
    return a + b
z=add(3, 5)
print(z)
#Q2 Take three arguments (Two of them are default) and return the product 
def multiply(a, b=2, c=3):
    return a * b * c
z=multiply(4)
print(z)
#Q3 Take variable number of arguments and return of them
def variable_sum(*args):
    return sum(args)

z=variable_sum(1, 2, 3, 4, 5)
print(z)
#Q4 Take two arguments and return three results (these arguments , square of the first, square of the second)
def square_values(a, b):
    return a, b, a**2, b**2
z=square_values(3, 4)
print(z)    