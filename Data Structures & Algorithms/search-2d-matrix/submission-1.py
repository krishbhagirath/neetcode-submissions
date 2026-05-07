class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        leftGroup = 0
        rightGroup = len(matrix) - 1

        while leftGroup <= rightGroup:
            midGroup =  (leftGroup + rightGroup) // 2

            if (target < matrix[midGroup][0]):
                rightGroup = midGroup - 1 # move the RG pointer left
            elif (target > matrix[midGroup][-1]):
                leftGroup = midGroup + 1 # move LG pointer right
            else:
                l = 0
                r = len(matrix[midGroup]) - 1

                while l <= r:
                    mid = (l + r) // 2

                    if (target > matrix[midGroup][mid]):
                        l = mid + 1
                    elif (target < matrix[midGroup][mid]):
                        r = mid - 1
                    else:
                        return True
                return False
        return False



    # log loop
        # loop rows
            # loop columns