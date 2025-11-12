from collections import Counter
from itertools import combinations, groupby, islice
import sys, re
import os


base_dir = os.path.dirname(__file__)
path = os.path.join(base_dir, "test.txt")

sys.stdin = open(path, "r")
def min_actions(s: str) -> int:
    #L’observation el mohema
    # Si andek 3 cellules ferghin wa7d b3d wa7d "...",
    #tnejm t7ot maa fi loula w l’akher (i-1 w i+1),
   #ba3d tna7i maa men eli fi wast (i),
   #w kol marra tna7i maa men cellule t3awadha b maa men juwarha —
   #ya3ni tnejm t3ebbi el kol b juste 2 actions .

    #Ama si ma fama 3 ferghin b3d b3d (ma fama "..."),
    #matnejmch ta3mel el 7araka hedhi,
    #fa ma3neha lazem t7ot maa fi kol cellule fergha wa7dha.
    empties = s.count('.')
    if empties == 0:
        return 0
    return 2 if '...' in s else empties

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())    
    s = input().strip()         
   
    print(min_actions(s))