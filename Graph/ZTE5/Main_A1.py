import numpy as np
from collections import Counter, defaultdict
import time
import copy
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def remove_node(G, target):
    del G[target]
    for nbrs in G.values():
        nbrs.discard(target)

def _unblock(thisnode, blocked, B):
    # 取消blocked, 并从B[thisnode]中删除节点
    stack = set([thisnode])
    while stack:
        node = stack.pop()
        if node in blocked:
            blocked.remove(node)
            stack.update(B[node])
            B[node].clear()

def namesLists(G1, Row, Len):
    NamesLists = []
    NamesPaths = []
    G = copy.deepcopy(G1)
    for startnode in range(Row):
        path = [startnode] # 当前路径中的节点堆栈
        blocked = set() # 顶点：被禁止搜索
        closed = set()  # nodes involved in a cycle 循环中涉及的节点
        blocked.add(startnode)
        # graph portions that yield no elementary circuit
        B = defaultdict(set) # 不产生循环的的图形部分
        stack = [(startnode, list(G[startnode]))]
        while stack:
            thisnode, nbrs = stack[-1]
            if nbrs:
                nextnode = nbrs.pop()
                canTran = nextnode not in blocked
                lenFalse = (len(path) != Len)
                if lenFalse and canTran:
                    path.append(nextnode)
                    stack.append((nextnode, list(G[nextnode])))
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
                elif lenFalse == False:
                    if nextnode == startnode:
                        NamesPaths.append(path[:])
                        Names = path[:]
                        Names.sort()
                        if Names not in NamesLists:
                            NamesLists.append(Names)
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
    return NamesLists, NamesPaths

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
    for num in [4, 6, 8, 10, 12, 14]:
        namesLists0, namesPaths0 = namesLists(G0, nRow, num)
        print(num, len(namesLists0), len(namesPaths0))
        tEndI = time.time()
        print(tEndI - tStart)
        Paths_file = 'ZTE5/Paths_0429_' + str(num) + '.txt'
        f = open(Paths_file, 'w')
        f.writelines(str(len(namesPaths0))+'\n')
        f.writelines(map(lambda x : ','.join([str(elem) for elem in x]) +'\n', namesPaths0))
        f.close()
        Lists_file = 'ZTE5/Lists_0429_' + str(num) + '.txt'
        f = open(Lists_file, 'w')
        f.writelines(str(len(namesLists0))+'\n')
        f.writelines(map(lambda x : ','.join([str(elem) for elem in x]) +'\n', namesLists0))
        f.close()