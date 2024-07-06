from numba import jit
lt,rt = map(int,input().split())
ls = list(map(str,input().split()))
rs = list(map(str,input().split()))
@jit
def result():
    result = [print("Yes") if i in rs else print("No") for i in ls]

result()
