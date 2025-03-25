# Problem: Binary Search - https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        high = len(nums) - 1
        low = 0
        mid = (high + low ) // 2
        while low <= high:
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                high = mid - 1
                mid = (high + low) // 2
            elif target > nums[mid]:
                low = mid + 1
                mid = (high + low) // 2
        return -1


        