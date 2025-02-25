# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

n = int(input())
for _ in range(n):
    m = int(input())
    arr = list(map(int, input().split()))
    max_sum = 0
    i = 0
    while i < m:
        j = i
        curr_max = arr[i]

        while j + 1 < m and (arr[j] > 0) == (arr[j + 1] > 0):
            curr_max = max(curr_max, arr[j + 1])
            j += 1
        
        max_sum += curr_max
        i = j + 1
    print(max_sum)