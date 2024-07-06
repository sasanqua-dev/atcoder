S = str(input())
rindex = S.rfind('R')
mindex = S.find('M')
if rindex > mindex:
    print('No')
else:
    print('Yes')