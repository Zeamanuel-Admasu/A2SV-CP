# Problem: Most Stones Removed with Same Row or Column - https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

class UnionFind:

    def __init__(self, stones):
        self.parent = []
        for i in range(len(stones)):
            self.parent.append(i)
        self.rank = [0 for i in range(len(stones))]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]
        return x

    def union(self, x, y):
        rootx, rooty = self.find(x), self.find(y)
       
        if self.rank[rootx] < self.rank[rooty]:
            self.parent[rootx] = rooty
        elif self.rank[rooty] < self.rank[rootx]:
            self.parent[rooty] = rootx
        else:
            self.parent[rooty] = rootx
            self.rank[rootx] += 1

    

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        row = defaultdict()
        col = defaultdict()
        uf = UnionFind(stones)
        for i in range(len(stones)):
            r, c = stones[i]
            if r in row:
                prev_stone = row[r]
                uf.union(i, prev_stone)
            else:
                row[r] = i
            if c in col:
                prev_stone = col[c]
                uf.union(i, prev_stone)
            else:
                col[c] = i

        parents_count = 0
        for i in range(len(stones)):
            if uf.parent[i] == i:
                parents_count += 1
        return len(stones) - parents_count


        