# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

def solve():
    n,k,q = map(int,input().split())
    queries = []
    minim = float("inf")
    maxim = float("-inf")
    for _ in range(n):
        l,r = map(int,input().split())
        minim = min(l,minim)
        maxim = max(r,maxim)
        queries.append((l,r)) 
    prefix = [0] * (maxim - minim + 2)
    for p in range(n):
        l,r = queries[p]
        prefix[l - minim] += 1
        prefix[r + 1 - minim] -= 1
    # print(prefix) 

    for i in range(1,len(prefix)):
        prefix[i] += prefix[i - 1]
    # print(prefix)

    another = [0] * len(prefix)

    for i in range(len(prefix)):
        if prefix[i] >= k:
            another[i] = 1
        if i > 0:
            another[i] += another[i - 1]
    for _ in range(q):
        l,r = (map(int,input().split()))
        l = max(l,minim)
        r = min(r,maxim)
        l -= minim
        r -= minim
        if l > r:
            print(0)
            continue
        if l != 0:
            
            print(another[r] - another[l - 1])
        else:
            print(another[r])
        
solve()