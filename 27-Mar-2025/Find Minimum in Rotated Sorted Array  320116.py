# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] <= nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]
        

        