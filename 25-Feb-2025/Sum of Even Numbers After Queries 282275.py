# Problem: Sum of Even Numbers After Queries - https://leetcode.com/problems/sum-of-even-numbers-after-queries/description/

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(elem for elem in nums if elem % 2 == 0)
        arr = []
        for val, idx in queries:
            old_value = nums[idx]
            if old_value % 2 == 0:
                even_sum -= old_value
            nums[idx] += val
            new_val = nums[idx]
            if new_val % 2 == 0:
                even_sum += new_val
            arr.append(even_sum)
        return arr
        