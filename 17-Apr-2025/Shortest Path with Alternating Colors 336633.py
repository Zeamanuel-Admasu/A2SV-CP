# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red = defaultdict(list)
        blue = defaultdict(list)

        for src, dst in redEdges:
            red[src].append(dst)
        for src, dst in blueEdges:
            blue[src].append(dst)

        answer = [-1 for i in range(n)]  
        queue = deque()
        queue.append([0, 0, None])
        visited = set()
        visited.add((0, None))    
        while queue:
            node, length, edgeColor = queue.popleft()
            if answer[node] == -1:
                answer[node] = length
            
            if edgeColor != "RED":
                for nbour in red[node]:
                    if (nbour, "RED") not in visited:
                        visited.add((nbour, "RED"))
                        queue.append([nbour, length + 1, "RED"])

            if edgeColor != "BLUE":
                for nbour in blue[node]:
                    if (nbour, "BLUE") not in visited:
                        visited.add((nbour, "BLUE"))
                        queue.append([nbour, length + 1, "BLUE"])
        return answer


