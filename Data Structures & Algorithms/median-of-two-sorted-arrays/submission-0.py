class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []

        for num in nums1:
            nums3.append(num)

        for num in nums2:
            nums3.append(num)
            
        nums3.sort()

        if (len(nums3) % 2 == 1):
            median = nums3[len(nums3) // 2]
        else:
            median = float(nums3[len(nums3) // 2] + nums3[(len(nums3) // 2) - 1]) / 2

        return median