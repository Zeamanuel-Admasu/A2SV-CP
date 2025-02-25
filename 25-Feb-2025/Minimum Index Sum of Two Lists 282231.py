# Problem: Minimum Index Sum of Two Lists - https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        list3 = []
        dict2 = {}
        list4 = []
        dict3 = {}
        for elem in list1:
            dict1[elem] = len(list3)
            list3.append(elem)
        for elem in list2:
            dict2[elem] = len(list4)
            list4.append(elem)
        for val in dict1:
            if val in dict2:
                dict3[val] = dict1[val] + dict2[val]
        min_val = min(dict3.values())
        min_keys = [key for key, value in dict3.items() if value == min_val]   
        return min_keys
            
        

        


        