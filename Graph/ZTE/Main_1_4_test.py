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

def g2DiaGs(G, Row):
    GCopy = copy.deepcopy(G)
    DiaGs = [] # 线结构
    key = 0
    pointsDict = defaultdict(list) # 按字典存储每条线上的点
    locationLine = defaultdict(list)
    for xStart in range(Row): # 遍历部落1
        for yStart in GCopy[xStart]: # 遍历xStart的好友列表
            step = 1 # 线的长度
            pointsDict[key].append([xStart, yStart]) # 按字典存储同一条线上的点
            while yStart+step in GCopy[xStart+step]:
                GCopy[xStart+step].discard(yStart+step) # 移除点, 避免线重复
                pointsDict[key].append([xStart+step, yStart+step]) # 按字典存储同一条线上的点
                step += 1 #线长度递增
            DiaGs.append([xStart, yStart, step]) # 保存线[起始X, 起始Y, 长度]
            locationLine[yStart-xStart].append(key) # 线位置
            key += 1
    return DiaGs, pointsDict, locationLine

def newCycle(G, pointsLines, Gps, Len):
    numNamesList = 0 # 名字列表的数量
    partNamesList = [] # 部分名字列表
    multNumsList = [] 
    GCopy = copy.deepcopy(G)
    for pointsLine in pointsLines: # 遍历每条线
        for i in range(pointsLine[2]):
        # 从起点开始
        i = 0
        namesList = []
        multNums = []
        startNode = pointsLine[0] + i
        secondNode = pointsLine[1] + i
        path = [startNode, secondNode]
        blocked = set((startNode, secondNode))
        closed = set()
        B = defaultdict(set)
        stack = [(secondNode, list(GCopy[secondNode]))]
        while stack:
            thisnode, nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
                canTran = nextnode not in blocked
                lenFalse = len(path) != Len
                if lenFalse and canTran:
                    path.append(nextnode)
                    stack.append((nextnode, list(GCopy[nextnode])))
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
                elif lenFalse == False:
                    if nextnode == startNode:
                        names = sorted(path)
                        if names not in namesList:
                            namesList.append(names)
                            partNamesList.append(names)
                            multNum = [Gps[path[i], path[i+1]] for i in range(len(path)-1)]
                            multNum.append(Gps[path[0], path[-1]])
                        # 定位的最小值
                        multNums.append(min(multNum))
                    closed.update(path)
            if not nbrs:
                if thisnode in closed:
                    _unblock(thisnode, blocked, B)
                else:
                    if thisnode in GCopy:
                        for nbr in GCopy[thisnode]:
                            if thisnode not in B[nbr]:
                                B[nbr].add(thisnode)
                stack.pop()
                path.pop()
        # remove_node(GCopy, startNode)
        if len(namesList) > 0:
            numNamesList += sum(multNums)
            multNumsList.append(multNums)
        for i in range(pointsLine[2]):
            GCopy[startNode+i].discard(secondNode+i)
            GCopy[secondNode+i].discard(startNode+i)
    return numNamesList, partNamesList, multNumsList

if __name__ == '__main__':
    mLoad = np.loadtxt('Example_0430.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    G0 = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                G0[i].add(j + nRow)
                G0[j + nRow].add(i)
    DiaG0, pointsDict, locationLine = g2DiaGs(G0, nRow)

    keyLinesX = [Dia[0] for Dia in DiaG0]
    keyLinesX = list(set(keyLinesX))
    keyLinesX.sort()
    keyLinesY = [Dia[1] for Dia in DiaG0]
    keyLinesY = list(set(keyLinesY))
    keyLinesY.sort()
    keyPoints = []
    for x in keyLinesX:
        for y in G0[x]:
            keyPoints.append([x, y])
    for y in keyLinesY:
        for x in G0[y]:
            keyPoints.append([x, y])

    # keyLinesX2 = [p[0] for p in keyPoints]
    # keyLinesX2 = list(set(keyLinesX2))
    # keyLinesX2.sort()
    # keyLinesY2 = [p[1] for p in keyPoints]
    # keyLinesY2 = list(set(keyLinesY2))
    # keyLinesY2.sort()
    # keyPoints2 = []
    # for x in keyLinesX2:
    #     for y in G0[x]:
    #         keyPoints2.append([x, y])
    # for y in keyLinesY2:
    #     for x in G0[y]:
    #         keyPoints2.append([x, y])
            
    pointClass = defaultdict(list)
    for keyPoint in keyPoints:
        for i in locationLine[keyPoint[1]-keyPoint[0]]:#pointsDict.keys():
            if keyPoint in pointsDict[i] and keyPoint not in pointClass[i]:
                pointClass[i].append(keyPoint)

    newDiaG0 = []
    newGps = defaultdict(int) # 点的定位字典，在线结构的倒数第n个位置
    for i in pointClass.keys():
        pointClass[i].sort()
        pointClassList = list(pointClass[i])
        for j in range(len(pointClassList)-1):
            # pointsSearch.append(pointClass,)
            lenStep = pointClassList[j+1][0] - pointClassList[j][0]
            pointClassList[j].append(lenStep)
            for k in range(lenStep):
                loc = int(lenStep) - int(k)
                newGps[pointClassList[j][0]+k, pointClassList[j][1]+k] = loc # 定位,最后一个点为1, 第一个点为step
                newGps[pointClassList[j][1]+k, pointClassList[j][0]+k] = loc # 新增 便于检索定位
        lenStep = DiaG0[i][0] + DiaG0[i][2] - pointClassList[-1][0]
        pointClassList[-1].append(lenStep)
        for k in range(lenStep):
            loc = int(lenStep) - int(k)
            newGps[pointClassList[-1][0]+k, pointClassList[-1][1]+k] = loc # 定位,最后一个点为1, 第一个点为step
            newGps[pointClassList[-1][1]+k, pointClassList[-1][0]+k] = loc # 新增 便于检索定位
        newDiaG0 += pointClassList

    pointNum = [newDia[-1] for newDia in newDiaG0]
    # print(sum(pointNum)) # 7872
    # print(max(pointNum)) # 82
    # print(max(newGps.values())) # 82
    
    N0, C0, multN = newCycle(G0, newDiaG0, newGps, 4)
    print(N0)
