X , Y = map(int,input().split())
S = input()
i = X -1
S_list = list(S)
S_list[i:Y] = S_list[i:Y][::-1]
print(*S_list,sep='')