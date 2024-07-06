X ,Y = map(int,input().split())

if X >= Y :
    ans = 0

else:
    d = Y - X
    ans = (d+9) // 10

print(ans)