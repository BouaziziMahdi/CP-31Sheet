import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")
sys.stdin = open(path, 'r')

def game_integer(n:int)-> str:
    if n % 3 ==0:
        return "Second"
    else :
        return "First" if((n +1) % 3 ==0  or (n-1 )% 3 ==0 ) else "Second"
# Read number of test cases
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(game_integer(n))