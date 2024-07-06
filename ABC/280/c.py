S = list(input())
T = list(input())
S.append('')
for s,t,c in zip(list(S),list(T),range(len(T))):
    if s == t:
        continue
    else:
        print(c+1)
        break

