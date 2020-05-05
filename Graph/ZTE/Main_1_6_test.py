import numpy as np
from collections import defaultdict, Counter
import time
import copy

def _unblock(thisnode, blocked, B):
    stack = set([thisnode])
    while stack:
        node = stack.pop()
        if node in blocked:
            blocked.remove(node)
            stack.update(B[node])
            B[node].clear()

def g2lineGs(partG, row):
    G1 = copy.deepcopy(partG)
    lineGs = [] # 线结构
    numLines = 0
    gps = defaultdict(int) # 定位
    for xStart in range(row): # 遍历部落1
        for yStart in list(G1[xStart]): # 遍历xStart的好友列表
            numLines +=1
            G1[xStart].discard(yStart)
            step = 1 # 线的长度
            while yStart+step in G1[xStart+step]:
                G1[xStart+step].discard(yStart+step) # 移除点, 避免线重复
                step += 1 #线长度递增
            lineGs.append([xStart, yStart, step, yStart-xStart]) # 保存线[起始X, 起始Y, 长度]
            for i in range(step):
                gps[xStart+i, yStart+i] = step - i
                gps[yStart+i, xStart+i] = step - i
    return lineGs, gps, numLines

def newCycle(G, lineGs, Gps, keyX, num):
    numNamesList = 0 # 名字列表的数量
    partPathList = [] # 部分名字列表
    G1 = copy.deepcopy(G)
    for line in lineGs: # 遍历每条线
        Xs = list(set(range(line[0], line[0]+line[2])) & set(keyX))
        Xs.sort()
        for i in range(len(Xs)-1):
        # i = 0 # 从起点开始
        # while i < line[2]:
            namesList = []
            multStep = []
            # startNode = line[0] + i
            startNode = Xs[i]
            steps_tmp = Xs[i+1]-Xs[i]
            # secondNode = line[1] + i
            secondNode = line[3] + startNode
            path = [startNode, secondNode]
            blocked = set((startNode, secondNode))
            closed = set()
            B = defaultdict(set)
            stack = [(secondNode, list(G1[secondNode]))]
            while stack:
                thisnode, nbrs = stack[-1]
                if nbrs:
                    nextnode = nbrs.pop()
                    canTran = nextnode not in blocked
                    lenFalse = len(path) != num
                    if lenFalse and canTran:
                        path.append(nextnode)
                        stack.append((nextnode, list(G1[nextnode])))
                        closed.discard(nextnode)
                        blocked.add(nextnode)
                        continue
                    elif lenFalse == False:
                        if nextnode == startNode:
                            names = path[:]
                            names.sort()
                            if names not in namesList:
                                namesList.append(names)
                                partPathList.append(path)
                                multN = [Gps[path[i], path[i+1]] for i in range(len(path)-1)]
                                multN.append(Gps[path[0], path[-1]])
                            # 定位的最小值
                            multStep.append(min(multN))
                        closed.update(path)
                if not nbrs:
                    if thisnode in closed:
                        _unblock(thisnode, blocked, B)
                    else:
                        if thisnode in G1:
                            for nbr in G1[thisnode]:
                                if thisnode not in B[nbr]:
                                    B[nbr].add(thisnode)
                    stack.pop()
                    path.pop()
            if len(multStep) > 0:
                # steps = min(multStep)
                countN = 0
                for s in multStep:
                    if s >= steps_tmp:
                        countN += 1
                numNamesList += steps_tmp * countN
            for n in range(steps_tmp):
                G1[startNode+n].discard(secondNode+n)
                G1[secondNode+n].discard(startNode+n)
    return numNamesList, partPathList

if __name__ == '__main__':
    mLoad = np.loadtxt('Example_0430.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    G0 = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                G0[i].add(j + nRow)
                G0[j + nRow].add(i)
    partG0 = defaultdict(set)
    for i in range(nRow):
        partG0[i] = G0[i]
    lineGs0, Gps0, numLines0 = g2lineGs(partG0, nRow)

    keyX0 = [Dia[0] for Dia in lineGs0]
    keyX0 = list(set(keyX0))
    keyX0.sort()
    keyY0 = [Dia[1] for Dia in lineGs0]
    keyY0 = list(set(keyY0))
    keyY0.sort()

    tStart = time.time()
    for num in [4, 6, 8, 10, 12, 14]:
        numNamesList, partNamesList = newCycle(G0, lineGs0, Gps0, keyX0, num)
        print(num, numNamesList)
        tEndI = time.time()
        print(tEndI - tStart)
