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


#Max Consecutive Ones

nums = [1,0,1,1,0,1,1,1,1,1]

    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        n = len(nums)
        
        for i in range(0, n):
            if nums[i] == 0:
                count = 0
            else:
                count+=1
                result = max(result, count)
                
        return result 
    
  


# Find Numbers with Even Number of Digits

def findNumbers(nums):

        dig=0
        
        for x in nums:
            count =0
            while x!=0:
                x//=10
                count+=1
            if count%2 ==0:
                dig+=1
                
        return dig   
nums =[555,901,482,1771]


findNumbers(nums)
