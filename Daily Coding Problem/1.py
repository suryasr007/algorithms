"""
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

def run(arr=[3,2,1,4,5,-6], k=9):
    # Hash map technique (https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/)
    s = set() 
      
    for i in range(0,len(arr)): 
        temp = k-arr[i]
        if (temp>=0 and temp in s): 
            print (arr[i], temp) 
        s.add(arr[i]) 
    return s


    # While Looping Eliminate the numbers higher than k
    # n = len(arr)/2 if len(arr)%2 == 0 else (len(arr)/2)+1
    # for i in range(n):
    #     if arr[i] > k:
    #         continue
    #     for j in arr[i+1:]:
            
    #         if arr[i]+ j == k:
    #             print(i,j)
    #             return True

    # return False


if __name__ == "__main__":
    run()