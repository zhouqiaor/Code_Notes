import numpy as np
from collections import Counter
from collections import defaultdict
import networkx as nx
import time
import copy
import threading
import multiprocessing
import timeit
import operator

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

def myCycle(Range):
    Cycles = []
    G = copy.deepcopy(GLoad)
    tStart = time.time()
    for startnode in Range:
        path = [startnode]
        blocked = set()# 顶点：被阻止搜索
        closed = set()# 循环中涉及的节点
        blocked.add(startnode)
        B = defaultdict(set)# 没有循环的图部分
        stack = [(startnode,list(G[startnode]))]
        while stack:
            thisnode, nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
                if len(blocked) > limit:
                    closed.update(path)
                elif nextnode == startnode:
                    if len(path) in range(4, limit+1, 2):
                        Cycles.append(path[:]) # yield path[:]
                    closed.update(path)
                elif nextnode not in blocked:
                    path.append(nextnode)
                    stack.append((nextnode, list(G[nextnode])))
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
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
    tEnd = time.time()
    print(tEnd - tStart)
    return Cycles

if __name__ == '__main__':
    mLoad = np.loadtxt('ZTE/Example.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    GLoad = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                GLoad[i].add(j + nRow)
                GLoad[j + nRow].add(i)
    limit = 5
    Cycles = myCycle(range(nRow))
    Cs = []
    for c in Cycles:
        if len(c) in range(4, limit):
            c.sort()
            if c not in Cs:
                Cs.append(c)
    len_cs = [len(c) for c in Cs]
    len_cs.sort()
    result = Counter(len_cs)
    print(result)
