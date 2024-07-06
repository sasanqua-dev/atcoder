N_int,L_int,W_int = map(int,input().split())
A_list = set(range(L_int))
result = 0
A_list_rem = A_list.remove

q = [[A_list_rem((a+i2)) for i2 in range((W_int+1)) if (a+i2) in A_list] for a in map(int,input().split())]

for i1 in range(L_int):
    if len(A_list) == 0:
        break
    a = min(A_list)
    for i in range((W_int+1)):
        if (a+i) in A_list:
            A_list_rem((a+i))
    result += 1
print(result)