class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}  # key: 26-tuple signature, value: list of words

        for i in range(len(strs)): # for each word in the list
            count = [0] * 26 # declare an empty alpha list
            for ch in strs[i]: # loop through every character
                count[ord(ch) - ord('a')] += 1  # assumes lowercase a–z -> increase each letter's corresponding cell by 1
            
            key = tuple(count) # makes list immutable (converted to tuple)

            if key not in buckets: # checks dictionary KEYS
                buckets[key] = [] # key is the tuple/list of 1s and 0s -> create empty list for words represented by that tuple
            buckets[key].append(strs[i]) # append current word


        return list(buckets.values())