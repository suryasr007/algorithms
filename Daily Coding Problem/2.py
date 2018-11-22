"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""

from functools import reduce
import math

def run(arr=[1,2,3,4,5]):

    # x = a*b*c*d
    # log(x) = log(a*b*c*d)
    # log(x) = log(a) + log(b) + log(c) +log(d)
    # x = antilog(log(a)+log(b)+log(c)+log(d))

    EPS = 1e-9
    product = list()    
    s = reduce(lambda x,y:x+math.log10(y), arr[1:],math.log10(arr[0]))


     for n in arr:
        product.append(int((EPS + pow(10.00, s - math.log10(n)))))


    return product


    # product = reduce((lambda x,y: x*y), arr)
    # if product != 0:
    #     return list(map(lambda x: int(product/x), arr))
    # else: return 0


if __name__ == "__main__":
    print(run())
