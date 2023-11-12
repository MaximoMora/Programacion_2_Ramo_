

def SumArrays(nums):
    index = 0
    copyNumbs = nums
    for i in range(0,len(nums)):
        print(i)
        for j in range(0,i):

            print("index: ", j)
            copyNumbs[i] += nums[j]
            
    print(copyNumbs)
            


SumArrays([1,2,3,4])