# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        s1_count = [0] * 26
        window_count = [0] * 26
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1
        print(s1_count)
        for i in range(len(s1)):
            window_count[ord(s2[i]) - ord('a')] += 1
        # print(window_count)
        if s1_count == window_count:
            return True
        for i in range(len(s1), len(s2)):
            window_count[ord(s2[i]) - ord('a')] += 1
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            # print("aaaa",window_count)
            # print(s1_count)
            if s1_count == window_count:
                return True

        return False