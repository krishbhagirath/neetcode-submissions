class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = 0
        seen = set()

        for i in range(len(nums)):
            seen.add(nums[i])

        for i in range(len(nums)):
            x = nums[i]
            if((x-1) in seen):
                continue
            else:
                currentVal = x
                currentLen = 1
                while((currentVal+1) in seen):
                    currentLen += 1
                    currentVal += 1

            if(currentLen > consec):
                consec = currentLen

        return consec