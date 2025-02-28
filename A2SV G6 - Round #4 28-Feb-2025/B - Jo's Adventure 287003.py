# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

a, b = map(int, input().split())
arr = list(map(int, input().split()))
arr1 = list(arr[::-1])
pref = [0] * len(arr)
for i in range(1, len(arr)):
    if arr[i] < arr[i-1]:
        pref[i] = pref[i-1] + abs(arr[i] - arr[i-1])
    else:
        pref[i] = pref[i-1]
pref2 = [0] * len(arr)
for i in range(1, len(arr1)):
    if arr1[i] < arr1[i-1]:
        pref2[i] = pref2[i-1] + abs(arr1[i] - arr1[i-1])
    else:
        pref2[i] = pref2[i-1]
pref2 = pref2[::-1]
for i in range(b):
    n, m = map(int, input().split()) 
    if n < m:
        print(pref[m-1] - pref[n-1])
    else: 
        print( abs(pref2[m-1] - pref2[n-1]))
        
            

