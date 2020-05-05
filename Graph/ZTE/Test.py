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

def myCycle(GLoad, startnode, Cycles):
    G = copy.deepcopy(GLoad)
    path = [startnode]
    blocked = set()# 顶点：被阻止搜索
    closed = set()# 循环中涉及的节点
    blocked.add(startnode)
    B = defaultdict(set)# 没有循环的图部分
    stack = [(startnode,list(G[startnode]))]
    while stack:
        thisnode, nbrs = stack[-1]
        if nbrs:
            nextnode = nbrs.pop() # 从所有邻居中pop出下一个传递对象
            canNext = nextnode not in blocked # 没有循环后 是否可以继续
            nowNext = len(path)%2==1 or len(path)<4 # 回到原部落/次数太少 继续传递 不判断
            if nowNext and canNext:
                path.append(nextnode)
                stack.append((nextnode, list(G[nextnode])))
                closed.discard(nextnode)
                blocked.add(nextnode)
                continue
            if nextnode == startnode:# 回到起点 中止
                Cycles.append(path[:])#yield path[:]
                closed.update(path)
            elif len(path) >= 8: # 已经传到第14个 且下一次无法传回 中止
                closed.update(path)
            elif canNext:
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

if __name__ == '__main__':
    # 读取
    mLoad = np.loadtxt('ZTE/Example.csv', dtype=int, delimiter=',')
    # 预处理
    nRow, nCol = mLoad.shape
    GLoad = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                GLoad[i].add(j + nRow)
                GLoad[j + nRow].add(i)
    # 并行设置
    manager = multiprocessing.Manager()
    GPool = manager.dict(GLoad)
    CyclesPool = manager.list()
    List = manager.list(range(nRow))
    # 并行计算
    start = timeit.default_timer()
    proc = [multiprocessing.Process(target=myCycle, args=(GPool, List, CyclesPool))]
    for p in proc:
        p.start()
    for p in proc:
        p.join()
    end = timeit.default_timer()
    print('multi processing time:', str(end-start), 's')
    Cs = []
    for c in CyclesPool:
        c.sort()
        if c not in Cs:
            Cs.append(c)
    len_cs = [len(c) for c in Cs]
    len_cs.sort()
    result = Counter(len_cs)
    print(result)
