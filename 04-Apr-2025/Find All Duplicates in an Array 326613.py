# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            while nums[i] != nums[nums[i] - 1]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]
        
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(nums[i])
        return res
       