# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        for num, freq in a.items():
            bucket[freq].append(num)
        ans = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans

       

        