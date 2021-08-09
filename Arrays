#Find the missing element between two arrays
#1

def find_missing(arr1, arr2):
    # Your solution here
    res=0
    for num in arr1+arr2:
        res^=num
        
        
    return res
    
#2
def find_missing(arr1, arr2):
    # Your solution here

    arr1.sort()
    arr2.sort()
    
    for num1, num2 in zip(arr1, arr2):
        if num1 != num2:
            return num1
        
    return arr1[-1]  
