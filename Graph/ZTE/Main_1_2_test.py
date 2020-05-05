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
import sys

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

def myCycle(Range, Len):
    Cycles = []
    Paths = []
    G = copy.deepcopy(GLoad)
    tStart = time.time()
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
                        Paths.append(path[:])
                        Names = sorted(path)
                        if Names not in Cycles:
                            Cycles.append(Names[:])
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
    tEnd = time.time()
    print(tEnd - tStart)
    return Cycles, Paths

if __name__ == '__main__':
    mLoad = np.loadtxt('ZTE/Example_0429.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    GLoad = defaultdict(set)
    GLoad0 = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                GLoad0[i].add(j)
                GLoad[i].add(j + nRow)
                GLoad[j + nRow].add(i)
    Cs, Ps = myCycle(range(nRow), 6)

    f = open('ZTE/result_0429_6.txt', 'w')
    f.writelines(str(len(Cs))+'\n')
    f.writelines(map(lambda x : ','.join([str(elem) for elem in x]) +'\n', Cs))
    f.close()

    f = open('ZTE/path_0429_6.txt', 'w')
    f.writelines(str(len(Ps))+'\n')
    f.writelines(map(lambda x : ','.join([str(elem) for elem in x]) +'\n', Ps))
    f.close()
    len_cs = [len(c) for c in Cs]
    result = Counter(len_cs)
    print(result)
