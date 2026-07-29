class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # create sliding window looping through s2 with window size = len(s1)
        # use hashmap to count freq in window, compare to hashmap of s1
        # use 'matches' variable to compare the two hashmaps, ensuring all 26 freqs match in both hashmaps

        # edge case
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0]*26, [0]*26 # use arrays instead of hashes
        
        # making initial freq 'hashes' for chars in s1/s2
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1 # maps to 1 of 26 indices
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = 0

        # count number of matching chars
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        # sliding window
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1

            l += 1


        return matches == 26