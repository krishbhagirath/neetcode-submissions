class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        charSet = set()
        longest = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1

            charSet.add(s[r])
            longest = max(longest, r - l + 1)

        
        return longest



        # max = 0
        # substring = True            
        
        # for i in range(len(s)):
        #     seen = set()
        #     innerIndex = 0
        #     substring = True

        #     while (i + innerIndex < len(s)):
        #         if (s[i + innerIndex]) in seen:
        #             break

        #         seen.add(s[i + innerIndex])
        #         innerIndex += 1
        
        #     if (innerIndex > max):
        #         max = innerIndex

        
        # return max


        # while l < r:
        #     if ()


        # start with first two pointers (l and r)
        # outer loop for l - while l < r and the current state is not substring
            # keep moving l fwd

            # else
            # while it is a substring
                # move r fwd, update max if greater than current > max
