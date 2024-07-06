number = int(input())
string = str(input())
string2 = list(string)
St = [0]
for i in range((len(string))):
    if (len(string)) == i:
        break

    if string[i] == "L":
        string2.insert(i,(i+1))
    else:
        string2.insert((i+1),(i+1))

string2 = [str(a) for a in string2]
print(" ".join(string2))