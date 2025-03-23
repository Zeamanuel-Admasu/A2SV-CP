# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    res = 0
    i = 1
    while i < len(arr):
        if arr[i] < arr[i-1]:
            count += 1
            i += 2
        else:
            i += 1   
    return count
t = int(input())
for i in range(t):
    print(solve())