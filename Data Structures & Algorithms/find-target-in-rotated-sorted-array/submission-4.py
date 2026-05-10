class Solution:
    def search(self, nums: List[int], target: int) -> int:
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

        half = ""

        if l == 0:
            # not rotated, search whole array
            l = 0
            r = len(nums) - 1
        else:
            if (target < nums[0]):
                half = "right"
                r = len(nums) - 1
            else:
                half = "left"
                l = 0

        while l <= r:
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1

