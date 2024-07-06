def main():
    N_int,L_int,W_int = map(int,input().split())
    A_list = set(range(L_int))
    a_list = []
    result = 0
 
    a = set(map(int,input().split()))
    for i in a:
        for i2 in range((W_int+1)):
            a_list.append((i+i2))
    A_list = A_list - set(a_list)
 
    for _ in range(L_int):
        if len(A_list) == 0:
            break
        a = min(A_list)
        for i in range((W_int+1)):
            if (a+i) in A_list:
                A_list.remove((a+i))
        result += 1
    return result

print(main())