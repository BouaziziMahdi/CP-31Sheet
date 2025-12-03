
import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")

sys.stdin = open(path, "r")

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())

    if n >= k and (n - k) % 2 == 0:
        print("YES")
    elif n % 2 == 0:   
        print("YES")
    else:
        print("NO")
