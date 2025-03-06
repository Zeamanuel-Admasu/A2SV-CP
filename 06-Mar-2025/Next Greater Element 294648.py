# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = defaultdict(int)
        for num in nums2:
            while stack and num >  stack[-1]:
                value = stack.pop()
                nextGreater[value] = num
            stack.append(num)
        
        # print(nextGreater)
        return [nextGreater[num] if num in nextGreater else -1 for num in nums1]