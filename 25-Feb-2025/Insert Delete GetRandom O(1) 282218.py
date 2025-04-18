# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/description/

class RandomizedSet:

    def __init__(self):
        self.data = {}
        self.list = []
        
        

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        self.data[val] = len(self.list)
        self.list.append(val)
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.data:
            return False
        index = self.data[val]
        last_element = self.list[-1]
        self.list[index], self.list[-1] = self.list[-1], self.list[index]
        self.data[last_element] = index
        self.list.pop()
        self.data.pop(val)
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()