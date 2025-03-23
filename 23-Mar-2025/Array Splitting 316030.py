# Problem: Array Splitting - https://codeforces.com/problemset/problem/1197/C

n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

leftOver = []
for i in range(1, len(arr)):
    leftOver.append(arr[i] - arr[i-1])

L = sorted(leftOver)
a = L[:len(L) - k + 1]
print(sum(a))
# maxim = max(leftOver)
# minim = min(leftOver)
# cost = maxim - minim
# print(cost)



