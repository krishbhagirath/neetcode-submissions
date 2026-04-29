class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        found = False

        while(not found):
            if ((numbers[l] + numbers[r]) > target):
                r = r - 1
            elif((numbers[l] + numbers[r]) < target):
                l = l + 1
            else:
                found = True
                return [l+1, r+1]