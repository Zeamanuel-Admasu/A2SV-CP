# Problem: Kuriyama Mirai's Stones - https://codeforces.com/contest/433/problem/B

t = int(input())
arr = list(map(int, input().split()))
a = int(input())
sort_arr = sorted(arr)

for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]

for i in range(1, len(arr)):
    sort_arr[i] = sort_arr[i - 1] + sort_arr[i]

for i in range(a):
    first, l, r = list(map(int, input().split()))
    if first == 1:
        if l == 1:
            print(arr[r - 1])
        else:
            print(arr[r - 1] - arr[l - 2])
    else:
        if l == 1:
            print(sort_arr[r - 1])
        else:
            print(sort_arr[r - 1] - sort_arr[l - 2])

