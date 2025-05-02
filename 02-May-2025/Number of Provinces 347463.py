# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, x):
        while x != self.root[x]:
            self.root[x] = self.root[self.root[x]]
            x = self.root[x]

        return self.root[x]

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
            rankx = self.rank[rootx]
            ranky = self.rank[rooty]

            if rankx > ranky:
                self.root[rooty] = rootx
            elif rankx < ranky:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
       
        n = len(isConnected)

        dsu = UnionFind(n)

        components = n

        for citya in range(n):
            for cityb in range(citya + 1, n):
                if isConnected[citya][cityb] == 1 and dsu.find(citya) != dsu.find(cityb):
                    dsu.union(citya, cityb)
                    components -= 1


  

        return components