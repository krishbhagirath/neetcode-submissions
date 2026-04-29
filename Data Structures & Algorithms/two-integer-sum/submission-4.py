class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums : [3,4,5,6]
        # target : 7
        # output : [0,1]

        seen = {}
        
        # [3,4,5,6]
        for index, value in enumerate(nums):
            complement = target - value

            if(complement in seen):
                return [seen[complement], index]
            seen[value] = index
            