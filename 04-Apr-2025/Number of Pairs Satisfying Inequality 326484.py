# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        arr = []
        for i in range(len(nums1)):
            arr.append(nums1[i] - nums2[i])
        
        def merge(lst1, lst2):
            count = 0
            i = 0
            j = 0
            while j < len(lst2) and i < len(lst1):
                if lst1[i] <= lst2[j] + diff:
                    count += len(lst2) - j
                    i += 1   
                else:
                    j += 1
            i = 0
            j = 0
            res = []
            while i < len(lst1) and j < len(lst2):
                if lst1[i] <= lst2[j]:
                    res.append(lst1[i])
                    i += 1
                else:
                    res.append(lst2[j])
                    j += 1
            while i < len(lst1):
                res.append(lst1[i])
                i += 1
            while j < len(lst2):
                res.append(lst2[j])
                j += 1
            return res, count


        def mergeSort(arr):
            if len(arr) == 1:
                return arr, 0
            n = len(arr)
            mid = n // 2
            left_half, left_count = mergeSort(arr[:mid])
            right_half, right_count = mergeSort(arr[mid:])
            merged, pair_count = merge(left_half, right_half)
            return merged, left_count + pair_count + right_count
        _, count = mergeSort(arr)
        return count


