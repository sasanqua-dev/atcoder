import numpy as np 
import math
K = int(input())
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

FK = factorization(K)
np_FK = np.array(FK)
kind = np_FK[:,0]
Number = max([i[0]*i[1] for i in np_FK])#9
MK = max(kind)#5
if int(MK) >= int(Number):
    print(int(MK))

else:
    print(int(Number))