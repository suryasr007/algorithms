def run(A=[2, 3, 7, 6, 8, -1, -10, 15]):
    m = max(A) #Storing maximum value 
    if m < 1: 
          
        # In case all values in our array are negative 
        return 1 
    if len(A) == 1: 
          
        #If it contains only one element 
        return 2 if A[0] == 1 else 1     
    l = [0] * m 
    for i in range(len(A)): 
        if A[i] > 0: 
            if l[A[i] - 1] != 1: 
                  
                #Changing the value status at the index of our list 
                l[A[i] - 1] = 1 
    for i in range(len(l)): 
          
        #Encountering first 0, i.e, the element with least value 
        if l[i] == 0:  
            return i+1
            #In case all values are filled between 1 and m 
    return i+2 
        
        # positive_elements = filter(lambda x:x > -1, arr)
        # positive_elements.sort()

        # non_duplicates = list(set(positive_elements))
        # for i in range(len(non_duplicates) - 1):
        #     if non_duplicates[i+1] != non_duplicates[i] + 1: 
        #         return non_duplicates[i] + 1
        # return non_duplicates[-1] + 1
    
if __name__ == "__main__":
    print(run())