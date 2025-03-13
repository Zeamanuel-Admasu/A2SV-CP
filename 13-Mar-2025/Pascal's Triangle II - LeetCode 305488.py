# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def helper(rowIndex):
            if rowIndex == 0:
                return [1]
            arr = [1] * (rowIndex + 1)
            ret = helper(rowIndex - 1)
            i = 1
            for i in range(rowIndex - 1):
                arr[i + 1] = ret[i] + ret[i + 1]
            return arr
        return helper(rowIndex)



        