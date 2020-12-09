class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in nums:
            if index<1 or i != nums[index-1]:
                nums[index] = i
                index +=1
        return index