import bisect
N,L,R = map(int,input().split())
A = list(map(int,input().split()))
RangeHalf = (L+R)/2
result = []
for a in A:
    if a<=L:
        result.append(str(L))
    elif L<a and a<R:
        result.append(str(a))
    else:
        result.append(str(R))

print(' '.join(result))
        

