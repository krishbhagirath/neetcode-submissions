class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # dictionary (value/index pairs)

        for i, x in enumerate(nums):
            need = target - x # 3
            if need in seen: # checks the keys of the dictionary for 'need'
                return [seen[need], i] # if seen, return i (current index) and seen[need] (index of seen number)
            seen[x] = i



            # 0   3
            # 1   4
            # 2   5
            # 3   6