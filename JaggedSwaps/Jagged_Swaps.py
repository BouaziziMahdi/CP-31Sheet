import os, sys


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")

def jagged_Swaps(arr: list, n: int) -> str:
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return "YES"
    return "NO"
    #if arr[0] == 1:
    #    return "YES"
    #return "NO"


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))   
    print(jagged_Swaps(arr, n))
