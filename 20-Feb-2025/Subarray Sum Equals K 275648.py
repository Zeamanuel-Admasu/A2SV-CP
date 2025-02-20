# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = defaultdict(int)
        count = 0
        for i in range(len(nums)):
            if i != 0:
                nums[i] += nums[i - 1]
            if nums[i] - k in memo:
                count += memo[nums[i] - k]
            if nums[i] == k:
                count += 1
            memo[nums[i]] += 1
        return count


        