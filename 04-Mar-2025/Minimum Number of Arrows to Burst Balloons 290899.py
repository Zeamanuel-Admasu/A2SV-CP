# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        temp = [(b, a, b) for a, b in points]
        temp.sort()
        j = 0
        count = 1
        print(temp)
        for i in range(1, len(points)):
            if temp[i][1] <= temp[j][2]:
                continue
            else:
                j = i 
                count += 1
                print("this is count",  count, temp[i])
        return count





        