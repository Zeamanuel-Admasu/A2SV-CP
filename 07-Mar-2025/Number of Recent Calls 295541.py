# Problem: Number of Recent Calls - https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.request = []
        
    def ping(self, t: int) -> int:
        self.request.append(t)
        while t - self.request[0] > 3000:
            self.request.pop(0)
        # print(self.request)
        return len(self.request)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)