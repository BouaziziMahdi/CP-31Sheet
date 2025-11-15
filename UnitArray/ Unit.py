from math import prod
import os, sys

base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")

def  unit_special_array(n:int ,array:list)->int:
    res = 0
    while True:
        s = sum(array)
        p = prod(array)
        
        if s >= 0 and p == 1:
            return res
        
        for i in range(len(array)):
            if array[i] == -1:
                array[i] = 1
                res += 1
                break
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(unit_special_array(n, arr))