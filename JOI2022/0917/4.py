N = int(input())
S = list(map(int,input().split()))

for i in range(N):
    r = S.count(i+1)
    if r != 2:
        print(i+1)
        break