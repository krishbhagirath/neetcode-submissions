class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # goal - use the array itself as a 'hash'

        # ideally, every number should be at index = value - 1
        # the first number out of place, its index is the lowest non-present +

        # ex: [3,4,1,-1]
        # ideal: [1,2,3,4] 
        # sort given array - [1, -1, 3, 4] --> we see that index 2 value's wrong
        # therefore answer is 2

        n = len(nums)

        # place each # in its correct position
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]: # keep swapping the current number while its still a valid number (1...n)
                j = nums[i] - 1 # j - index where number belongs
                nums[i], nums[j] = nums[j], nums[i] # swap


        # search for the number that's incorrectly placed
        for i in range(n):
            if nums[i] != i + 1: # if the current number != index + 1
                return i + 1

        return n + 1 # length + 1 is first missing positive
        