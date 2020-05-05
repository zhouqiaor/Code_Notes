import numpy as np
from collections import Counter, defaultdict
import time
import copy
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

if __name__ == '__main__':
    mLoad = np.loadtxt('ZTE5/Example_0429.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    G0 = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                G0[i].add(j + nRow)
                G0[j + nRow].add(i)
    tStart = time.time()

    lenBlock = 64 # rBlock = nRow // lenBlock
    sumCol = np.sum(mLoad, axis=0)
    combList = [int(math.factorial(i)/(2*math.factorial(i-2))) 
    for i in range(2, max(sumCol)+1)]
    num = 4 # for num in [4, 6, 8, 10, 12, 14]:
    N = 0
    for x1 in range(nRow - lenBlock):
        nB = x1 // lenBlock
        for x2 in range((nB + 1) * lenBlock, nRow):
            lFinded = len(G0[x1] & G0[x2])
            if lFinded > 1:
                N += combList[lFinded - 2]
    tEndI = time.time()
    print(tEndI - tStart)
    print(N)