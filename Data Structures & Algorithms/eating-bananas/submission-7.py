class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # binary search is performed on POSSIBLE EATING SPEEDS
        # eating speeds can be anywhere from 1 (min) to max value of piles

        l = 1
        r = max(piles)

        while l <= r:
            hours = 0
            k = (l + r) // 2 # middle value

            for pile in piles:
                hours += math.ceil(pile/k) # calculate hours needed to complete
            
            if hours <= h:
                # if we took less time than required (or equal), look at left half
                result = k # this value works, store in result
                r = k - 1 # keep checking for a potentially better speed (smaller value)
            elif hours > h:
                l = k + 1


        return result
