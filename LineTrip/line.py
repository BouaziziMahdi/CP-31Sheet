from collections import Counter
from itertools import combinations, groupby, islice
import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")

sys.stdin = open(path, "r")


#data = list(map(int, input().split()))
#ata = list(map(int, input().split()))
def minimum_possible_volume(stations, x):
    stations = sorted(stations)
    arr = [0] + stations + [x]
    #gaps = []
    #for i in range(len(arr) - 1):
    #gaps.append(arr[i + 1] - arr[i])
    gaps = [arr[i+1] - arr[i] for i in range(len(arr)-1)]
    max_gap = max(gaps)
    last_gap = gaps[-1]
    return max(max_gap, 2 * last_gap)

t = int(input().strip())
for _ in range(t):
    n, x = map(int, input().split())
    if n > 0:
        a = list(map(int, input().split()))
    else:
        a = []           
        _ = input() if False else None  
    print(minimum_possible_volume(a, x))