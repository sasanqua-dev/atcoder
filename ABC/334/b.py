import numpy as np
A,M,L,R = map(int,input().split())
if A>0:
    if A<L:
        st = M*((R-A)//M)+A
        ed = M*((L-A)//M+1)+A
    elif A>R:
        st = M*(((R-A)//M)*-1-1)+A
        ed = M*(((L-A)//M)*-1+1)+A
    else:
        st = M*((R-A)//M)+A
        ed = M*(((L-A)//M)*-1)+A
else:
    if A<L:
        st = M*((R-A)//M)+A
        ed = M*((L-A)//M-1)+A
    elif A>R:
        st = M*(((R-A)//M)*-1+1)+A
        ed = M*(((L-A)//M)*-1-1)+A
    else:
        st = M*((R-A)//M)+A
        ed = M*(((L-A)//M)*+1)+A

if ((ed-st)//M+1) < 0:
    print(((ed-st)//M+1)*-1)
else:
    print((ed-st)//M+1)