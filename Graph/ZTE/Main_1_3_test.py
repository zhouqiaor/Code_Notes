import numpy as np
from collections import defaultdict, Counter
import time
import copy
# import threading
# import multiprocessing

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
    # Gps = defaultdict(int) # 点的定位字典，在线结构的倒数第n个位置
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
            # for i in range(step):
            #     Gps[xStart+i, yStart+i] = step - i # 定位,最后一个点为1, 第一个点为step
            #     Gps[yStart+i, xStart+i] = step - i # 新增 便于检索定位
    # DiaGs.sort(key=lambda x: (x[0],x[1])) # 按点位置排序
    return DiaGs, pointsDict, locationLine#, Gps

""" def m2DiaGs(M):
    Row, Col = M.shape
    DiaGs = [] # 线结构
    Gps = defaultdict(int) # 点的定位字典，在线结构的倒数第n个位置
    for xStart in range(Row-1): # 遍历部落一
        for yStart in range(Col-1):
            if M[xStart][yStart] == 1:
                step = 1 # 线长度2.0
                while M[xStart+step][yStart+step] == 1:
                    step += 1 # 满足条件, 线长度递增
                DiaGs.append([xStart, yStart, step]) # 保存斜线[起始X, 起始Y, 长度]
                for i in range(step):
                    Gps[xStart+i, yStart+i] = step - i # 定位,最后一个点为1, 第一个点为step
                    Gps[yStart+i, xStart+i] = step - i # 新增 便于检索定位
    DiaGs.sort(key=lambda x: (x[0],x[1])) # 按点位置排序
    return DiaGs, Gps 
"""

""" def newDiaGs(G, keyPointsX, keyPointsY):
    DiaGs = [] # 线结构
    for i in range(len(keyPointsX)-1):
        for j in range(len(keyPointsY)-1):
            if keyPointsY[j] in G[keyPointsX[i]]:
                stepLimit = min(keyPointsX[i+1]-keyPointsX[i], keyPointsY[j+1]-keyPointsY[j])
                step = 1 # 线长度2.0
                while step < stepLimit-1 and keyPointsY[j+step] in G[keyPointsX[i+step]]:
                    step += 1 # 满足条件, 线长度递增
                DiaGs.append([keyPointsX[i], keyPointsY[j], step])
    return DiaGs """

""" 
def newCycle(G, pointsLines, Gps, Len):
    numNamesList = 0 # 名字列表的数量
    partNamesList = [] # 部分名字列表
    multNumsList = [] 
    GCopy = copy.deepcopy(G)
    for pointsLine in pointsLines: # 遍历每条线
        for i in range(pointsLine[2]): # 在线上遍历
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
                                # 所有点的定位2.0
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
            GCopy[startNode].discard(secondNode)
            GCopy[secondNode].discard(startNode)
            if len(namesList) > 0:
                numNamesList += sum(multNums)
                multNumsList.append(multNums)
                for i in range(1, multNums[-1]):
                    GCopy[secondNode+i].discard(startNode+i)
                    GCopy[startNode+i].discard(secondNode+i)
                break
    return numNamesList, partNamesList, multNumsList """

def newCycle(G, pointsLines, Gps, Len):
    numNamesList = 0 # 名字列表的数量
    partNamesList = [] # 部分名字列表
    multNumsList = [] 
    GCopy = copy.deepcopy(G)
    for pointsLine in pointsLines: # 遍历每条线
        # for i in range(pointsLine[2]): # 在线上遍历
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
                            # 所有点的定位2.0
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
                # GLoad0[i].add(j)
                G0[i].add(j + nRow)
                G0[j + nRow].add(i)
    DiaG0, pointsDict, locationLine = g2DiaGs(G0, nRow)
    # DiaG0, Gps0 = g2DiaGs(G0, nRow)
    # DiaG01, Gps01 = m2DiaGs(mLoad)

    keyLinesX = [Dia[0] for Dia in DiaG0]
    keyLinesX = list(set(keyLinesX))
    keyLinesX.sort()
    keyLinesY = [Dia[1] for Dia in DiaG0]
    keyLinesY = list(set(keyLinesY))
    keyLinesY.sort()
    # for i in range(len(keyPointsY)):
    #     keyPointsY[i] -= nRow
    keyPoints = []
    for x in keyLinesX:
        for y in G0[x]:
            keyPoints.append([x, y])
    for y in keyLinesY:
        for x in G0[y]:
            keyPoints.append([x, y])

    # for DiaG in DiaG0:
    #     P = keyPoints[:][:]
    #     xRange = range(DiaG[0], DiaG[0]+DiaG[2])
    #     yRange = range(DiaG[1], DiaG[0]+DiaG[2])
    pointClass = defaultdict(list)
    for keyPoint in keyPoints:
        for i in locationLine[keyPoint[1]-keyPoint[0]]:#pointsDict.keys():
            if keyPoint in pointsDict[i] and keyPoint not in pointClass[i]:
                pointClass[i].append(keyPoint)

    # pointsSearch = []
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
    # DiaGs.sort(key=lambda x: (x[0],x[1])) # 按点位置排序
                
    # DiaG1 = newDiaGs(G0, keyPointsX, keyPointsY)

    N0, C0, multN = newCycle(G0, newDiaG0, newGps, 4)
    print(N0)
    # worse = 0
    # for i in range(len(newDiaG0)):
    #     if newDiaG0[i][2] == 0:
    #         worse += 1
    # lenNewDiaG0 = [len(NewDia) for NewDia in newDiaG0]
    # Counter(lenNewDiaG0)