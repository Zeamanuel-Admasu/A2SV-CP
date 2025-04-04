# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def yigerem(time):
            ranks.sort()
            total_cars = 0
            for i in range(len(ranks)):
                cur_cars = int(math.sqrt(time // ranks[i]))
                total_cars += cur_cars
                if total_cars >= cars:
                    return True
            return False

        left = 0
        right = max(ranks) * cars * cars
        while left <= right:
            mid = (left + right) // 2
            if yigerem(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left



        