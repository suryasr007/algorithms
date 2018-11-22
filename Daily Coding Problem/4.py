"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def run(A=[2, 3, 7, 6, 8, 1, -10, 15]):
    m = max(A) #Storing maximum value 
    if m < 1: 
          
        # In case all values in our array are negative 
        return 1 
    if len(A) == 1: 
          
        #If it contains only one element 
        return 2 if A[0] == 1 else 1     
    l = [0] * m 
    for e in A: 
        if e > 0: 
            if l[e - 1] != 1: 
                  
                #Changing the value status at the index of our list 
                l[e - 1] = 1 
    for i in range(len(l)): 
          
        #Encountering first 0, i.e, the element with least value 
        if l[i] == 0:  
            return i+1
            #In case all values are filled between 1 and m 
    return i+2 
    
if __name__ == "__main__":
    print(run())