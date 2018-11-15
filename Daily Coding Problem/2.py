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
