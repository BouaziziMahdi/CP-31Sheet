import os, sys
from typing import List


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")


def sequence_game(arr: List[int]) -> List[int]:
    res = []
    n = len(arr)
    res.append(arr[0])
    for i in range(1, n):
        if arr[i] >= arr[i - 1]:
            res.append(arr[i])
        else:
            res.append(arr[i])
            res.append(arr[i])

    return res


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    ans = sequence_game(arr)
    print(len(ans))
    print(*ans)


