class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        x = len(nums1)
        y = len(nums2)
        if x > y :
            return self.findMedianSortedArrays(nums2, nums1)
        start = 0
        end = x
        isFound = False
        isEven = True if (x+y) % 2 == 0 else False
        
        MIN = -10**7
        MAX = 10**7

        while start <= end:
            partitionX = (start + end) // 2
            partitionY = ((x + y + 1) // 2) - partitionX

            maxLeftX = MIN if partitionX == 0 else nums1[partitionX - 1]
            minRightX = MAX if partitionX == x else nums1[partitionX]

            maxLeftY = MIN if partitionY == 0 else nums2[partitionY - 1]
            minRightY = MAX if partitionY == y else nums2[partitionY]

            if (maxLeftX <= minRightY and maxLeftY <= minRightX) :
                if isEven is True :
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                else :
                    return max(maxLeftX, maxLeftY)

                # return value
            else:
                if maxLeftX > minRightY :
                    end = partitionX - 1
                else :
                    start = partitionX + 1

s = Solution()
print ("Solution is ", s.findMedianSortedArrays([1,2, 3], [4, 5]))


                

