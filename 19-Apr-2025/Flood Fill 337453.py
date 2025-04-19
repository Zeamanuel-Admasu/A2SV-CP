# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        cur_color = image[sr][sc]
        directions = [[0,-1], [0,1], [1,0],[-1,0]]
        def dfs(sr, sc):
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and image[sr][sc] == cur_color and image[sr][sc] != color:
                image[sr][sc] = color
                for i,j in directions:
                    nr = sr + i
                    nc = sc + j
                    dfs(nr, nc)
        dfs(sr, sc)
        return image


        