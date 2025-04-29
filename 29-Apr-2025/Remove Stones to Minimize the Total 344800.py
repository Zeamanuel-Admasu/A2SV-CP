# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] = -1 * piles[i]
        
        # heap = []
        # for i in range(len(piles)):
        #     heappush(heap, piles[i])
        
        heapify(piles)
        
        for i in range(k):
            val = -1 * heappop(piles)
            val -= val // 2
            heappush(piles, -1 * val)
        return -1 * sum(piles)
            
            

        