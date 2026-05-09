class Solution:
    def findMin(self, nums: List[int]) -> int:
        ## O(n) brute force
        # min = 100000
        # for num in nums:
        #     if num < min:
        #         min = num
        # return min

        ## O(log n)

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if (nums[mid] > nums[r]):
                # middle is greater than end, i.e. mistake is in right half as array SHOULD ascend, but does not
                l = mid + 1
            elif (nums[mid] < nums[r]):
                # mid is less than r, right half is sorted, mistake in left
                r = mid

        return nums[l]

        