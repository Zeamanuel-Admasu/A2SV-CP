# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)):
            diff = costs[i][0] - costs[i][1]
            costs[i].append(diff)
        sorted_arr = sorted(costs, key=lambda x:x[2])
        print(sorted_arr)
        ans1 = 0
        half = int(len(costs) // 2)
        i = 0
        while half != 0:
            ans1 = sorted_arr[i][0] + ans1
            half -= 1
            i += 1
            print(ans1)
        ans2 = 0
        
        while half <= int(len(costs) // 2) - 1:
            ans2 = sorted_arr[i][1] + ans2
            half += 1
            i += 1
            print(ans2)
        total = ans1 + ans2
        return total



        #     len()
        # print(sorted_arr)
         

        