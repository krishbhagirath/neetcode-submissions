class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums : [3,4,5,6]
        # target : 7
        # output : [0,1]



        seen = {} # tracks seen indices

        for i in range(len(nums)):
            desired = target - nums[i]

            if desired in seen:
                return [seen[desired], i]
            
            seen[nums[i]] = i

        return False




















        # seen = {}

        # for i in range (len(nums)):
        #     num = nums[i]
        #     desiredNum = target - num

        #     if desiredNum in seen:
        #         return [seen[desiredNum], i] # seen[desiredNum] is the index desiredNum is at in nums, i is the index that num is at in nums

        #     seen[num] = i



































        # seen = {}
        
        # # [3,4,5,6]
        # for index, value in enumerate(nums):
        #     complement = target - value

        #     if(complement in seen):
        #         return [seen[complement], index]
        #     seen[value] = index
            