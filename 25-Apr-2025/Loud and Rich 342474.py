# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        graph = defaultdict(list)
        indegree = [0] * len(quiet)
        ans = [i for i in range(len(quiet))]
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        queue = deque()
        
        for i in range(len(quiet)):
            if indegree[i] == 0:
                queue.append(i)
        print(queue)
        count = 0
        while queue:
            node = queue.popleft()
            count += 1
            for nbr in graph[node]:
                if quiet[ans[node]] < quiet[ans[nbr]]:
                    ans[nbr] = ans[node]
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
                print(count, queue)
                
        return ans

        
        

        