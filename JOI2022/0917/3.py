N = int(input())
S = list(map(int,input().split()))

S = list(S)
now = 0
answer = 0

for i in range(N):
    trans = S[i]
    if trans == "L":
        now = now -1
        if now < 0:
            now = 0
    
    else:
        now = now + 1
        if now > 2:
            now = 2
    
    if now == 2:
        answer += 1

print(answer)


