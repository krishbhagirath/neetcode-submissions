class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums);

        for i in range(len(nums)):
            for n in range(len(nums)):
                if (n != i):
                    result[i] *= nums[n]
            
        
        return result
            
        

        