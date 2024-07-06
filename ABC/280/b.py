N = input()
S = list(map(int,input().split()))
A = []

count = 0
for i in S:
    A.append(int(S[count]) - sum(A))
    count += 1

print(*A)