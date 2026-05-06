class Solution(object):
    def twoSum(self, nums, target):
        store1 = 0
        store2 = 0
        for i in range(len(nums)):
            for k in range(i+1,len(nums)):
                check = nums[i]+nums[k]
                if check == target:
                    store1= i
                    store2= k

        return [store1,store2]
          
        
        
