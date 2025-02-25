# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

n = int(input())
for _ in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    i = 0
    while i < m:
        curr_max = arr[i]

        while i + 1 < m and (arr[i] > 0) == (arr[i + 1] > 0):
            curr_max = max(curr_max, arr[i + 1])
            i += 1
        
        max_sum += curr_max
        i += 1
    print(max_sum)