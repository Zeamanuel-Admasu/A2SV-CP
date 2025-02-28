# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

def solve():
    n = int(input())
    a = input()
    b = input()
    one1 = 0
    one2 = 0
    zero1,zero2 = 0,0
    same = True
    for i in range(n):
        if a[i] == b[i]:
            if not same:
                return "NO"
            # same = True            
        else:    
            if same:
                if not (zero1 == one1):
                    return "NO"
            same = False
        if a[i] == "0":
            zero1 += 1
        else:
            one1 += 1
        if b[i] == "0":
            zero2 += 1
        else:
            one2 += 1 
        if a[i] != b[i]:
            if zero1 == one1:
                same = True
    if not (zero1 == zero2 and one1 == one2):
        return "NO"
    return "YES"
for _ in range(int(input())):
    print(solve())