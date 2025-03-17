# Problem: Books - https://codeforces.com/contest/279/problem/B

n, t = list(map(int, input().split()))
nums = list(map(int, input().split()))

j = 0
maxim = 0
curr = 0

for i in range(n): 
    while j < n and curr + nums[j] <= t: 
        curr += nums[j]
        j += 1
    maxim = max(maxim, j - i) 
    curr -= nums[i] 
print(maxim)