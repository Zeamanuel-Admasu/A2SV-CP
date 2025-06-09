# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res = []
        def backtrack(curr):
            if len(curr) == n:
                res.append("".join(curr))
                return
            curr.append("1")
            backtrack(curr)
            curr.pop()
            if not curr or curr[-1] != "0":
                curr.append("0")
                backtrack(curr)
                curr.pop()
        backtrack([])
        return res

