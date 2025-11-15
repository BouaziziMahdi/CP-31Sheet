import os, sys
from collections import Counter 

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")


def shizuku_special_move(n:int )->int:
    if(n%2==1):
           return 0
    return n//4+1

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(shizuku_special_move(n))

    