N , K , Q = map(int,input().split())
A = list(map(int,input().split()))
L = list(map(int,input().split()))

l = [0] * N
for i in A:
    l[i-1] = 1

Aa = A 

for ip,a in zip(range(Q),L):
    i = Aa[a-1]
    if (i == N):
        pass

    elif (l[i] == 1):
        pass
        

    else:
        l[i-1] = 0
        l[i] = 1
        Aa[a-1] = Aa[a-1] + 1

ans = []
for i in range(N):
    if l[i] == 1:
        ans.append(i+1)

print(*ans)