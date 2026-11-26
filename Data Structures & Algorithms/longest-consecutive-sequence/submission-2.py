class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        consec = 0
        seen = set()


        for num in nums:
            seen.add(num)

        for i in range(len(nums)):
            x = nums[i]

            if ((x-1) in seen): # not the start of a seq
                continue
            else:
                currVal = x
                currLen = 1

                while (currVal+1) in seen:
                    currVal += 1
                    currLen += 1
                

            if currLen > consec:
                consec = currLen

        
        return consec
                




        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # consec = 0
        # seen = set()

        # for i in range(len(nums)):
        #     seen.add(nums[i])

        # for i in range(len(nums)):
        #     x = nums[i]
        #     if((x-1) in seen):
        #         continue
        #     else:
        #         currentVal = x
        #         currentLen = 1
        #         while((currentVal+1) in seen):
        #             currentLen += 1
        #             currentVal += 1

        #     if(currentLen > consec):
        #         consec = currentLen

        # return consec