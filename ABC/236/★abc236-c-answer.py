local_train,rappid_train = map(int,input().split())
local_station = list(map(str,input().split()))
rappid_station = set(list(map(str,input().split())))
result = [print("Yes") if i in rappid_station else print("No") for i in local_station]