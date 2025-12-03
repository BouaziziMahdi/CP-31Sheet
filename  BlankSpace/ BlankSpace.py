import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")

sys.stdin = open(path, "r")

def is_blank_space(s:list)->int:
    if not s:
        return []
    res=[]
    current_blank=[s[0]]
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            current_blank.append(s[i])
        else:
            res.append(current_blank)
            current_blank=[s[i]]
    res.append(current_blank)
    return res
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    blank_spaces = is_blank_space(a)

    zero_lengths = []
    for space in blank_spaces:
        if space[0] == 0:          
            zero_lengths.append(len(space))

    print(max(zero_lengths) if zero_lengths else 0)