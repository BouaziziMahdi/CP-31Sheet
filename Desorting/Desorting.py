
import os, sys

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")
def Desorting(arr:list)->int:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return 0
    min_gap = float('inf')
    for i in range(len(arr) - 1):
        gap = arr[i+1] - arr[i]
        min_gap = min(min_gap, gap)
    return (min_gap // 2) + 1

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(Desorting(arr))

            