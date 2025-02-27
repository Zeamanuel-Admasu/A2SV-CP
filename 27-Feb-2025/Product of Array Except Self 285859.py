# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        arr1 = []
        prod = 1
        for i in range(len(nums)):
            if i != 0:
                prod = prod * nums[i-1]
            arr1.append(prod)
        
        arr2 = []
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            if i != (len(nums) - 1):
                prod = prod * nums[i+1]
            arr2.append(prod)
        arr2 = arr2[::-1]
        for i in range(len(arr2)):
            arr2[i] = arr2[i] * arr1[i]
        
        return arr2
        
        


        