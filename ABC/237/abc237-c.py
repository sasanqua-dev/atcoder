string = input()
count_back_a = 0
count_front_a = 0
if string == string[::-1]:
    print("Yes")
    exit()

for i in range(len(string)):
    if string[(-1*(i+1))] == "a":
        count_back_a += 1
    else:
        break

for i in range(len(string)):
    if string[i] == "a":
        count_front_a += 1
    else:
        break

count_a = count_back_a - count_front_a
if count_a < 0:
    print("No")
    exit()

result_str = "a"*count_a + string
if result_str == result_str[::-1]:
    print("Yes")
else:
    print("No")