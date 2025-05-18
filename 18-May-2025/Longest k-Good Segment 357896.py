# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

count = defaultdict(int)
left = 0
max_len = 0
left_ans = 1
right_ans = 1
unique = 0

for right in range(n):
    count[arr[right]] += 1
    if count[arr[right]] == 1:
        unique += 1

    while unique > k:
        count[arr[left]] -= 1
        if count[arr[left]] == 0:
            unique -= 1
        left += 1

    if right - left + 1 > max_len:
        max_len = right - left + 1
        left_ans = left + 1
        right_ans = right + 1

print(left_ans, right_ans)
