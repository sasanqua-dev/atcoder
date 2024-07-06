import math
N , X = map(int,input().split())
STR = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = int(math.ceil((X / N)))
answer = STR[number-1:number]
print(answer)