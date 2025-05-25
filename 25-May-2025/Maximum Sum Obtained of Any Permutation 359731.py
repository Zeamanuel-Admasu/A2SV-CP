# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0] * (len(nums) + 1)
        for a, b in requests:
            freq[a] += 1
            freq[b + 1] -= 1
        for i in range(1, len(nums)):
            freq[i] = freq[i] + freq[i - 1]
        freq = freq[:len(nums)]
        # print(freq)
        a = sorted(freq, reverse = True)
        b = sorted(nums, reverse = True)
        total = 0
        for i in range(len(nums)):
            total += a[i] * b[i]
        return (total) % ((10 ** 9) + 7)






        