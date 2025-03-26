# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def Yigerem(capacity):
            count = 0
            num_days = 1
            for weight in weights:
                if count + weight > capacity:
                    num_days += 1
                    count = weight
                else:
                    count += weight
            return num_days <= days




        left = max(weights)
        right = sum(weights)
        while left <= right:
            mid = (left + right)//2
            if Yigerem(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        