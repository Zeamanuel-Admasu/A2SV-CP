# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        memo = defaultdict(int)
        count = 0
        memo[count] = 1
        res = 0
        for i in range(len(nums)):
            count += nums[i]
            if (count % k) in memo:
                res += memo[count % k]
            memo[count % k] += 1
        return res


        