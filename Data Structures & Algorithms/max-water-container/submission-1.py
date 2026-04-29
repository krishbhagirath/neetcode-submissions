class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        currentArea = 0
        max = 0
        
        # area = (index2 - index1) * min(heights[index2], heights[index1])

        while(l < r):
            currentArea = (r - l) * min(heights[l], heights[r])

            # find the currentarea
            # compare to max, overwrite max if greater
            # after, move the pointer (l or r) that has the shorter bar (as that one may find a larger bar)

            # loop

            if(currentArea > max):
                max = currentArea
            
            if(heights[l] < heights[r]):
                l += 1
            else:
                r -= 1


        return max


        