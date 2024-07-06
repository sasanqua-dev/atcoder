S = str(input())
T = str(input())
l = [[0,1,2,2,1],[1,0,1,2,2],[2,1,0,1,2],[2,2,1,0,1],[1,2,2,1,0]]
SS = l[ord(S[0])-65][ord(S[1])-65]
TT = l[ord(T[0])-65][ord(T[1])-65]
if abs(SS) == abs(TT):
    print("Yes")
else:
    print("No")