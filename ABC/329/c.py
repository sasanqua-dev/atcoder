N = int(input())
S = str(input())
dic = {}
count=0
for s,index in zip(S,range(len(S))):
    if s == S[index-1]:
        count += 1
    else:
        if S[index-1] in dic:
            if dic[S[index-1]] < count:
                dic[S[index-1]] = count
        else:
            dic[S[index-1]] = count
print(sum(dic.values()))