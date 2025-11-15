
import os, sys
base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, "r")

def missing_efficiency(effs):
    total = sum(effs)   
    
    return -total   
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    efficiencies = list(map(int, input().split()))
    print(missing_efficiency(efficiencies))