"""
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""
def countWaysUtil(n,m): 
    res = [0]*n # Creates list res witth all elements 0 
    res[0],res[1] = 1,1
      
    for i in range(2,n): 
        j = 1
        while j<=m and j<=i: 
            res[i] = res[i] + res[i-j] 
            j = j + 1 
    return res[n-1] 

def run(s, m):
    print(countWaysUtil(s+1, m))


if __name__ == "__main__":
    run(4, 4)