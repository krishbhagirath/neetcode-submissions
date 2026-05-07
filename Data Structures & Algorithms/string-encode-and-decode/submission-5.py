class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""

        for word in strs:
            out += str(len(word)) + ":" + word

        return out

    # Encode: for each word, add current string + length of word (int) + colon + the word itself
    # Ex: "4:word8:neetcode6:coding"

        
    def decode(self, s: str) -> List[str]:
        words = []
        i = 0
        
        while i < len(s):
            colon = s.find(':', i) # find the colon, starting from i
            length = int(s[i:colon]) # store number in length (value between i (inclusive) and colon (exclusive))
            words.append(s[colon+1 : colon+1+length]) # append the letters from after colon to that pos + length
            i = colon + 1 + length # move index to the end of the word
        return words

    # Decode:
    # - create empty list, init index
    # - loop over every character
    #       - each time, find colon and store index, extract length number, append extracted word, move index forward
            
                