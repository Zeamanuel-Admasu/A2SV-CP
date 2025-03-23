# Problem: Find Consecutive Integers from a Data Stream - https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        

    def consec(self, num: int) -> bool:
        # print(self.queue)
        if num == self.value:
            self.queue.append(num)
            if len(self.queue) == self.k:
                self.queue.popleft()
                return True
            return False    
        else: 
            self.queue = deque()
            return False
        


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)