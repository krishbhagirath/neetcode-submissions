class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0        
        count = {}
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) # increment count by 1

            while (r - l + 1) - max(count.values()) > k: # length of window - maxfreq in the current window
                count[s[l]] -= 1 # decrement count of left before moving fwd
                l += 1 # move l fwd

            res = max(res, r - l + 1) # on each loop of r, result is the max of existing result OR current window               

        return res
