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
        # B的作用是记录因为此点阻塞而被迫阻塞的顶点
        # 一旦点i因为调用unblock过程解锁
        # 那么在B[i]链表中记录的顶点也因此解锁
        # B的效果是将每个点尽可能的保持阻塞状态以防止重复搜索
        B = defaultdict(set)# 没有循环的图部分
        stack = [(startnode,list(G[startnode]))]
        while stack:
            thisnode, nbrs = stack[-1]#当前node及其nbrs
            if nbrs:
                nextnode = nbrs.pop() # 从所有邻居中pop出下一个传递对象
                canTran = nextnode not in blocked # 没有循环后 是否可以继续
                # lenFalse = (len(path)%2 == 1) or (len(path) < 4) # 回到原部落/次数太少 继续传递 不判断
                lenFalse = len(path) not in range(4, 9, 2)
                if lenFalse and canTran:
                    path.append(nextnode) # 路径list
                    stack.append((nextnode, list(G[nextnode]))) # 下一个node及其nbrs入栈
                    closed.discard(nextnode)
                    blocked.add(nextnode) # nextnode已遍历锁定
                    continue
                if nextnode == startnode: # 回到起点 中止
                    Names = sorted(path) # 排序
                    if Names not in Cycles: # 是否存在
                        Cycles.append(Names) # yield path[:] # 保存/返回循环
                    closed.update(path) # 循环节点全部关闭
                elif len(path) >= 8: # 已经传到第14个 且下一次无法传回 中止
                    closed.update(path) # 超出规定长度 全部关闭
                elif canTran:
                    path.append(nextnode)
                    stack.append((nextnode, list(G[nextnode])))
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
            if not nbrs:
                # 如果能够在thisnode的邻接顶点中找到一条环路，则f就是true的
                # 这时可以把thisnode解锁，即调用_unblock过程。
                if thisnode in closed:
                    _unblock(thisnode, blocked, B)
                # 反之，则说明从包含从thisnode出发的边的路径都是死路，是不可能的形成环的
                # 所以不能解锁thisnode，同时要把与v邻接的顶点置于B数组的第thisnode个链表中
                # 经过thisnode的路径是死路，但经过thisnode的邻接顶点w的不一定死路
                # 应为w可能有另外的上级顶点
                # 所以如果不搜索thisnode了，即解锁thisnode顶点是要把B[thisnode]中记录的顶点也解锁，以供其他路径搜索使用。
                else:
                    if thisnode in G:
                        for nbr in G[thisnode]:
                            if thisnode not in B[nbr]:
                                B[nbr].add(thisnode)
                # 对thisnode的调用结束时把thisnode出栈。返回f，标志在这次调用中是否发现环。
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
    Cs = myCycle(range(nRow))
    len_cs = [len(c) for c in Cs]
    len_cs.sort()
    result = Counter(len_cs)
    print(result)
