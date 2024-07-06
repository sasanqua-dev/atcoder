import numpy as np
N = int(input())
XY = np.array([list(map(int, input().split())) for _ in range(N)])
if XY[:, 0].sum() > XY[:, 1].sum():
    print("Takahashi")
elif XY[:, 0].sum() == XY[:, 1].sum():
    print('Draw')
else:
    print("Aoki")
