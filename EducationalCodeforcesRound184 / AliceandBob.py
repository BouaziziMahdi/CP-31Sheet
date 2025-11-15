import sys, re
import os

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, 'r')


def alice_and_bob(n, a, array):
    cntLess = 0     
    cntGreater = 0  

    for x in array:
        if x < a:
            cntLess += 1
        elif x > a:
            cntGreater += 1

    if cntLess > cntGreater:
        b = a - 1
    else:
        b = a + 1

    return b

t = int(input().strip())
for _ in range(t):
    n, a = map(int, input().strip().split())
    array = list(map(int, input().strip().split()))
    print(alice_and_bob(n, a, array))

