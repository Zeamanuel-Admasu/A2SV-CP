# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        for i in range(len(nums) + 1):
            xor ^= i
        return xor

        