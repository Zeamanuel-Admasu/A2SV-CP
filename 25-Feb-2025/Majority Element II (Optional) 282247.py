# Problem: Majority Element II (Optional) - https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dict1 = Counter(nums)
        pivot = len(nums) / 3
        arr = []
        for item, count in dict1.items():
            if count > pivot:
                arr.append(item)
        return arr
        