V,A,B,C = map(int,input().split())
if V < A :
    print("F")

elif V < (A+B):
    print("M")

elif V < (A+B+C):
    print("T")

else:
    a = V % (A+B+C) 
    if a < A :
        print("F")

    elif a < (A+B):
        print("M")

    elif a < (A+B+C):
        print("T")   