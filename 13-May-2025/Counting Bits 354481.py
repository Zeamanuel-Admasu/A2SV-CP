# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            binn = []
            while i != 0:
                rem = i % 2
                binn.append(rem)
                i = i // 2
            a = Counter(binn)
            ans.append(a[1])
        return ans

            
        