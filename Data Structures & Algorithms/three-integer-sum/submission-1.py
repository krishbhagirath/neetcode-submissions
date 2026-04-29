class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() # sort the list first
        #[-1,0,1,2,-1,-4] --> [-4,-1,-1,0,1,2]

        for i in range(len(nums)): # iterate over every number (this is the fixed index)
            if (i > 0 and nums[i] == nums[i-1]): # skip any duplicate i's
                continue
            
            # init l and r
            l = i + 1 
            r = len(nums) - 1

            # keep looping (everything AFTER i index) while l and r don't cross
            while l < r: 
                if (nums[i] + nums[l] + nums[r] > 0): # move r back if target is positive
                    r -= 1
                elif (nums[i] + nums[l] + nums[r] < 0): # move l fwd if target is negative
                    l += 1
                elif (nums[i] + nums[l] + nums[r] == 0): # found a triplet
                    ans.append([nums[i], nums[l], nums[r]]) # append to ans list

                    # first, increment l, decrement r
                    l += 1
                    r -= 1

                    # if same index again for either, keep moving
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1                    

        return ans