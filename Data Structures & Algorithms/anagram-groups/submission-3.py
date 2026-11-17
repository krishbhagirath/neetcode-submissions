class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {} # 1. create empty dictionary for all groups

        # 2. create freq table for each word, anagrams have matching freq table

        for word in strs:
            freq = [0] * 26
            
            for char in word:
                val = ord(char) - ord('a')
                freq[val] += 1
            
            # here we have freq array for a given word
        
            key = tuple(freq) # 3. converts freq list into tuple
                              # list CANNOT be a key to a dictionary
                              # turns {0,1,1,0...} into (0,1,1,0...)
                              # now tuple version of freq can be a key

            if key not in groups: # 4. IN keyword looks at KEYS of groups, not the values - check first
                groups[key] = []
            
            groups[key].append(word) # 5. append word to given freq table key
        

        return list(groups.values()) # 6. return list of the VALUES in each group