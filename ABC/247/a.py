L = [0,0,0,0]
A = map(str,input().split())
for i in range(3):
    if A[i] == 1:
        L[i+1] = 1

print(''.join(map(str, L)))