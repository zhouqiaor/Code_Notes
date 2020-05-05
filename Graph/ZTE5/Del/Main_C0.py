import numpy as np
from collections import Counter, defaultdict
import time
import copy
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def g2lineGs(G, row):
    G1 = copy.deepcopy(G)
    lineGs = [] # 线结构
    numLines = 0
    # gps = defaultdict(int) # 定位
    for xStart in range(row): # 遍历部落1
        for yStart in list(G1[xStart]): # 遍历xStart的好友列表
            numLines +=1
            G1[xStart].discard(yStart)
            step = 1 # 线的长度
            while yStart+step in G1[xStart+step]:
                G1[xStart+step].discard(yStart+step) # 移除点, 避免线重复
                step += 1 #线长度递增
            lineGs.append([xStart, xStart+step, yStart-row, yStart+step-row, yStart-xStart-row]) # 保存线[起始X, 起始Y, 长度]
            # for i in range(step):
            #     gps[xStart+i, yStart+i] = step - i
            #     gps[yStart+i, xStart+i] = step - i
    return lineGs, numLines

if __name__ == '__main__':
    mLoad = np.loadtxt('ZTE5/Example_0429.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    G0 = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                G0[i].add(j + nRow)
                G0[j + nRow].add(i)
    lineGs0, numLines0 = g2lineGs(G0, nRow)
    print(numLines0)

    xdDit = defaultdict(list)
    # xD = np.zeros((numLines0, numLines0))
    ydDit = defaultdict(list)
    # yD = np.zeros((numLines0, numLines0))
    for i in range(numLines0):
        for j in range(i+1, numLines0):
            ixS = lineGs0[i][0]
            ixE = lineGs0[i][1]
            jxS = lineGs0[j][0]
            jxE = lineGs0[j][1]
            iyS = lineGs0[i][2]
            iyE = lineGs0[i][3]
            jyS = lineGs0[j][2]
            jyE = lineGs0[j][3]
            if (ixS-jxE)*(ixE-jxS) <= 0:
                dis = lineGs0[i][4] - lineGs0[j][4]
                # xD[i][j] = dis
                # xD[j][i] = -xD[i][j]
                xdDit[dis].append([i, j])
                xdDit[-dis].append([j, i])
            if (iyS-jxE)*(iyE-jyS) <= 0:
                dis = lineGs0[i][4] - lineGs0[j][4]
                # yD[i][j] = dis
                # yD[j][i] = -yD[i][j]
                ydDit[dis].append([i, j])
                ydDit[-dis].append([j, i])
            # else:
            #     xD[i][j] = None
            #     xD[j][i] = None
            #     yD[i][j] = None
            #     yD[j][i] = None
        # D[i][i] = None
    
    # A = (D != None)
    # print(sum(sum(A)))
    # plt.matshow(xD)
    # plt.show()
    # print(D)
