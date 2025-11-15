import os, sys

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")

def kid(array: list, n: int) -> int:
    res = []
    for x in array:
        res.append(abs(x))
    return min(res)
n = int(input().strip())
arr = list(map(int, input().split()))
print(kid(arr, n))