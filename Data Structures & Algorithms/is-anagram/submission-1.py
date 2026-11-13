class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq_s = {}

        if len(s) != len(t):
            return False

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1 # defaults to 0 if that key does not exist
        for char in t:
            freq_s[char] = freq_s.get(char, 0) - 1

        for value in freq_s.values():
            if value != 0:
                return False
            
        return True































        # if len(s) != len(t):
        #     return False

        # frequency = [0] * 26  #26 letters in alphabet
        
        # for letter in s:
        #     frequency[ord(letter) - ord('a')] += 1
        # for letter in t:
        #     frequency[ord(letter) - ord('a')] -= 1
        
        # for element in frequency:
        #     if element != 0:
        #         return False
        
        # return True