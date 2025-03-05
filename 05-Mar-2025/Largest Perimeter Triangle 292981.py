# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        i = 0
        j = 1
        k = 2
        count = 0
        while k < len(nums):
            if nums[k] + nums[j] > nums[i]:
                return nums[i] + nums[j] + nums[k]
            i += 1
            j += 1
            k += 1
        return 0



                      
                    