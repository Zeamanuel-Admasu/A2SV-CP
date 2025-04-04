# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for num in nums:
            num = abs(num)
            nums[num - 1] = abs(nums[num - 1]) * -1
        
        for num1 in nums:
            num1 = abs(num1)
            nums[num1 - 1] = nums[num1 - 1] * -1
        
        arr = []
        for i in range(len(nums)):
            if nums[i] < 0:
                arr.append(i + 1)
            else:
                continue
        return arr



        