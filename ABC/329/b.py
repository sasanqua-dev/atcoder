N = int(input())
A = set(map(int,input().split()))
Adash = sorted(A,reverse=True)
print(Adash[1])