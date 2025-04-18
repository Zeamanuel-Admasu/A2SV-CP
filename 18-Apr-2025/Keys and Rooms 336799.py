# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = {0}
        while queue:
            room = queue.pop()
            for key in rooms[room]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)
        return len(visited) == len(rooms)


        