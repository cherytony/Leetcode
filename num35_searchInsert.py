class Solution:

    def searchInsert(self, nums, target):

        for i, j in enumerate(nums):

            if j < target:
                continue
            else:
                return i

        return len(nums)



