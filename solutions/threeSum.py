import itertools

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        finalList = []
        for i in range(0, len(nums) - 2):
            for j in range(i+1, len(nums) - 1):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l = [nums[i], nums[j], nums[k]]
                        l.sort()
                        print("New list is ", l)
                        finalList.append(l)

        finalList.sort()
        return list(finalList for finalList, _ in itertools.groupby(finalList))

s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))