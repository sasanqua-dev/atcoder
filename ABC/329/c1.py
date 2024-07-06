N = int(input())
S = str(input())
result = []
current = ""

for char in S:
    if not current or char == current[-1]:
        current += char
    else:
        result.append(current)
        current = char
if current:
    result.append(current)
result = [max(filter(lambda x: x.startswith(c), result), key=len) for c in set(map(lambda x: x[0], result))]
print(len(''.join(result)))