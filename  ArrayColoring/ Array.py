
import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")

def ArrayColoring(arr):
    colorArray=[]
    for i in range (len(arr)):
        if arr[i]%2==1:
            colorArray.append(arr[i]) 
        sum_odd=(sum(colorArray)%2)==0
    if sum_odd:
        return "YES"
    else:
        return "NO"

sys.stdin = open(path, "r")
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(ArrayColoring(arr))
    
            