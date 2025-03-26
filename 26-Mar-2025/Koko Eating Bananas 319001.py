# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def Yigerem(pile):
            hours = 0
            for bananas in piles:
                hours += ceil(bananas / pile)

            return hours <= h

        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            if Yigerem(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low

        