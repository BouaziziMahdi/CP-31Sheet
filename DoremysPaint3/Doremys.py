import os, sys
from collections import Counter 

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")

def is_good(arr):
    n = len(arr)
    count = Counter(arr)
    if len(count) == 1:
        return True
    if len(count) == 2:
        half = n // 2
        return any(c == half for c in count.values())
    return False

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    print("YES" if is_good(a) else "NO")