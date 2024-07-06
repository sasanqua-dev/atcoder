K = int(input())
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))

if N < M:
    rl = [a for a in A for b in B if (a + K == b)]
else:
    rl = [b for b in B for a in A if (b - K == a)]
print(len(rl))