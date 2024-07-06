S = input()
a,b = map(int,input().split())
ast = S[a-1]
bst = S[b-1]
R1 = S[0:(a-1)]
R2 = S[(a):(b-1)]
R3 = S[(b):]
print(R1+bst+R2+ast+R3)