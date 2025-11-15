from collections import Counter
from itertools import combinations, groupby, islice
import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")

sys.stdin = open(path, "r")

 

A, B, C, D = map(int, input().split())

if C >= A and D < B:
    print("Yes")
else:
    print("No")