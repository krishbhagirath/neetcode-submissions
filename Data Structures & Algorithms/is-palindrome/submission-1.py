class Solution:
    def isPalindrome(self, s: str) -> bool:

        # declare pointers, l at 0, r at end
        l = 0
        r = len(s) - 1

        # run while l and r don't cross
        while (l < r):
            
            # move l fwd until its alphanumeric
            while l < r and not((s[l] >= 'a' and s[l] <= 'z') or (s[l] >= 'A' and s[l] <= 'Z') or (s[l] >= '0' and s[l] <= '9')):
                l += 1
            
            # move r bwd until its alphanumeric
            while l < r and not((s[r] >= 'a' and s[r] <= 'z') or (s[r] >= 'A' and s[r] <= 'Z') or (s[r] >= '0' and s[r] <= '9')):
                r -= 1
            
            # compare string's l and r indices - continue if match, break if not
            if (s[l].lower() == s[r].lower()):
                l += 1
                r -= 1
            else:
                break

        # if cross occurred, its a palindrome, else not
        if l >= r:
            return True
        else:
            return False

    