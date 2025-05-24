# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        count = 0
        res = 0
        for i in range(len(nums)):
            count += nums[i]
            if count - k in memo:
                res += memo[count - k]
            memo[count] += 1
        return res
            




        