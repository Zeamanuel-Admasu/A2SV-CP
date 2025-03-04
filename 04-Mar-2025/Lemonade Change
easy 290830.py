# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = []
        for num in bills:
            if num == 5:
                change.append(5)
            elif num == 10:
                if 5 in change:
                    change.remove(5)
                    change.append(10)
                else:
                    return False
            elif num == 20:
                if 5 in change and 10 in change:
                    change.remove(5)
                    change.remove(10)
                elif change.count(5) >= 3:
                    change.remove(5)
                    change.remove(5)
                    change.remove(5)
                else:
                    return False
        return True

        