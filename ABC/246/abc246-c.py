N,K,X = map(int,input().split())
A = list(map(int,input().split()))
k = K
L = [None]
for i in L:
    if (k == 0) or (A is None):
        break
    
    n = max(A)
    A.remove(n)

    if n < X:
        k -= 1     

    else:
        k = k - n//X
        A.append(n%X)

    L.append(None)    
print(sum(A))