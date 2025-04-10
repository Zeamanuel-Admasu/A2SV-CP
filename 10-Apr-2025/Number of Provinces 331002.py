# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edge_list = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and i != j:
                    edge_list[i].append(j)
        white = 1
        grey = 2
        color = [white] * len(isConnected[0])
        # print(color)
        count = 0
        def dfs(node):
            # nonlocal count
            color[node] = grey
            for i in (edge_list[node]):
                if color[i] == white:
                    dfs(i)
                    # return
        for i in range(len(isConnected)):
            if color[i] == white:
                dfs(i)
                count += 1
        return count



        