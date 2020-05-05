import numpy as np
from collections import Counter, defaultdict
import copy
import time

def remove_node(G, target):
    del G[target]
    for nbrs in G.values():
        nbrs.discard(target)

def _unblock(thisnode, blocked, B):
    stack = set([thisnode])
    while stack:
        node = stack.pop()
        if node in blocked:
            blocked.remove(node)
            stack.update(B[node])
            B[node].clear()

def myCycle(GLoad, Range, Len):
    Cycles = []
    G = copy.deepcopy(GLoad)
    for startnode in Range:
        path = [startnode]
        blocked = set()
        closed = set()
        blocked.add(startnode)
        B = defaultdict(set)
        stack = [(startnode, list(G[startnode]))]
        while stack:
            thisnode, nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
                canTran = nextnode not in blocked
                lenFalse = len(path) != Len
                if lenFalse and canTran:
                    path.append(nextnode)
                    stack.append((nextnode, list(G[nextnode])))
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
                elif lenFalse == False:
                    if nextnode == startnode:
                        Names = sorted(path)
                        if Names not in Cycles:
                            Cycles.append(Names)
                    closed.update(path)
            if not nbrs:
                if thisnode in closed:
                    _unblock(thisnode, blocked, B)
                else:
                    if thisnode in G:
                        for nbr in G[thisnode]:
                            if thisnode not in B[nbr]:
                                B[nbr].add(thisnode)
                stack.pop()
                path.pop()
        remove_node(G, startnode)
    return Cycles

def printNums(filedir, numList):
    mLoad = np.loadtxt(filedir, dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    GLoad = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                GLoad[i].add(j + nRow)
                GLoad[j + nRow].add(i)
    tStart = time.time()
    for num in numList:
        Cs = myCycle(GLoad, range(nRow), num)
        len_cs = [len(c) for c in Cs]
        result = Counter(len_cs)
        print(result)
        tEnd = time.time()
        print(tEnd - tStart)

