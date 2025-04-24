# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        rev_graph = [[] for _ in range(len(graph))]
        incoming = [0 for _ in range(len(graph))]

        for u in range(len(graph)):
            for v in graph[u]:
                rev_graph[v].append(u)
                incoming[u] += 1
        queue = deque()
        final = []
        for elem, ind in enumerate(graph):
            if ind == []:
                queue.append(elem)
                final.append(elem)
        print(queue)
        while queue:
            node = queue.popleft()
            for nbr in rev_graph[node]:
                incoming[nbr] -= 1
                if incoming[nbr] == 0:
                    queue.append(nbr)
                    final.append(nbr)
        final.sort()
        return list(final)
