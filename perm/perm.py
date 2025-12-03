import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")

sys.stdin = open(path, "r")

t = int(input())
for _ in range(t):
    n = int(input())
    b = []
    a = list(map(int, input().split()))
    for x in a:
       b.append(n + 1 - x)
    print(' '.join(map(str, b)))