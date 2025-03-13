# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        Array = []
        for row in range(rowIndex + 1):
            newRow = [1] * (row + 1)
            for j in range (1, row):
                newRow[j] = Array[row - 1][j - 1] + Array[row - 1][j]
            Array.append(newRow)
        return Array[rowIndex]


        