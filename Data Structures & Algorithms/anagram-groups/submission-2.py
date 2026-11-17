class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}

        # create freq table for each word, anagrams have matching freq table

        for word in strs:
            freq = [0] * 26
            
            for char in word:
                val = ord(char) - ord('a')
                freq[val] += 1
            
            # here we have freq array for a given word
        
            key = tuple(freq) # converts freq list into tuple
                              # list CANNOT be a key to a dictionary
                              # turns {0,1,1,0...} into (0,1,1,0...)
                              # now tuple version of freq can be a key

            if key not in groups: # IN keyword looks at the KEYS of groups, not the values
                groups[key] = []
            
            groups[key].append(word)
        

        return list(groups.values())