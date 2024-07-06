import bisect
N,L = map(int,input().split())
A = list(map(int,input().split()))

A.sort(reverse=True)
result = 0
for a in A:
    if a >= L:
        result+= 1
    else:
        break
print(result)