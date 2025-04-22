# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            x, y = equations[i]
            value = values[i]
            graph[x].append((y, value))
            graph[y].append((x, 1 / value))

        def dfs(curr, target, total, visited):
            if curr == target:
                return total
            visited.add(curr)
            for nbr, weight in graph[curr]:
                if nbr not in visited:
                    res = dfs(nbr, target, total * weight, visited)
                    if res != -1:
                        return res
            return -1

        answers = []
        for x, y in queries:
            if x not in graph or y not in graph:
                answers.append(-1)
                continue
            answer = dfs(x, y, 1, set())
            answers.append(answer)
        
        return answers
        