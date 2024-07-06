import numpy as np
N,K = map(int,input().split())
A = list(map(int,input().split()))
numbers = np.arange(1, N + 1)
ballot = np.repeat(numbers, 2)
def remove_elements(ar1, ar2):
    for item in ar2:
        mask = (ar1 == item)
        if np.count_nonzero(mask) > 1:
            indices_to_remove = np.where(mask)[0][0]
            ar1 = np.delete(ar1, indices_to_remove)
        else:
            ar1 = ar1[ar1 != item]
    return ar1
def remove_duplicate_elements(ar1):
    unique_elements, counts = np.unique(ar1, return_counts=True)
    duplicate_elements = unique_elements[counts > 1]
    for item in duplicate_elements:
        ar1 = ar1[ar1 != item]
    return ar1

arr = remove_duplicate_elements(remove_elements(ballot,A))
if (arr.size) % 2 != 0:
    arr = arr[:-1]
pairs = arr.reshape(-1, 2)
print(np.sum(np.abs(np.diff(pairs, axis=1).reshape(-1))))