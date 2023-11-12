
def TwoSum( nums, target):
    firtsNumber = 0 
    secondNumber = 0
    for i in range(0,len(nums)):  
        for j in range(0,len(nums)): 
            if nums[i] + nums[j] == target:
                firtsNumber = j
                secondNumber = i
                break
                
    return firtsNumber, secondNumber


result = TwoSum([2,4,11,3],6)
print(result)
                
        