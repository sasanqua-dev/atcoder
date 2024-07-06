list_x = []
list_y = []
for i in range(3):
  a = list(map(int,input().split()))
  list_x.append(a[0])
  list_y.append(a[1])

def col(list):
  for i2 in list:
    if (list.count(i2) == 1):
      return i2

print(col(list_x),col(list_y))
    