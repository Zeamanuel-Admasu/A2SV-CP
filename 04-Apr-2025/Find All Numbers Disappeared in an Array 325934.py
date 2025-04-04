# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
                correct = nums[i] - 1
                nums[i], nums[correct] = nums[correct], nums[i]
        ans = []
        for i in range(len(nums)):
            if nums[i] - i != 1:
                ans.append(i+1)
        return ans

        