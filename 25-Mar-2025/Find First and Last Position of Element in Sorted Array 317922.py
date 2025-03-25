# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]
        low = 0
        high = len(nums) - 1
        arr = []
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
        print(low, high)
        if low < len(nums) and nums[low] == target:
            arr.append(low)
        else:
            arr.append(-1)

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target: 
                high = mid - 1
            else:
                low = mid + 1
        if high > -1 and nums[high] == target:
            arr.append(high)
        else:
            arr.append(-1)
        return arr

        
        
            


        
        