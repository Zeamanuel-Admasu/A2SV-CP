# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answers.sort()
        a = Counter(answers)
        b = sum(a.values())
        count = 0
        for x, y in a.items():
            if x >= y:
                count += x + 1
            else:
                count += ceil(y/(x+1)) * (x+1)


        return count
            



        print(b)
        print(a)
        return 1
        