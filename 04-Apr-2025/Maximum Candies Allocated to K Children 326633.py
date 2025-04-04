# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0
        def yigerem(c):
            val = 0
            
            for i in range(len(candies)):
                # print(candies[i], c)
                val += candies[i] // c
            # print(val)
            if val >= k:
                return True
            else:
                return False
            
        left = 1
        right = max(candies)
        while left <= right:
            mid = (left + right) // 2
            if yigerem(mid):
                left = mid + 1
            else:
                right = mid - 1
                
        return right


        