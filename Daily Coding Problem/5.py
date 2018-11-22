"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
Implement car and cdr.
"""

def cons(a, b):
    # Takes the parameters as input
    def pair(f):
        # Takes function as input and runs the recieved function
        return f(a, b)
    
    return pair

def car(f):
    # Takes function as input
    def left(a, b):
        return a
    # pass the left function to the called function
    return f(left)

def cdr(f):
    def right(a, b):
        return b
    return f(right)




print(car(cons(2,3))) # Passing cons function to car function
print(cdr(cons(2,3)))