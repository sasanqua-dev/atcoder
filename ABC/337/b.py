import re
S = str(input())


def check_ABC(string):
    pattern = r'^(A+B+C+|A+|B+|C+)$'
    match = re.fullmatch(pattern, string)
    if match:
        return "Yes"
    else:
        return "No"


print(check_ABC(''.join(sorted(set(S), key=S.index))))
