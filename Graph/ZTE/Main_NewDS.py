import numpy as np
import scipy.sparse as ss
import matplotlib.pyplot as plt
from collections import Counter
from collections import defaultdict
import time
import copy

# new data structure
def g2DiaGs(G, Row):
    diaGs = []
    # myG2 = []
    G_ = copy.deepcopy(G)
    for xStart in range(Row):
        xAdj = G_[xStart]
        for yStart in xAdj:
            step = 0
            while yStart+step+1 in G_[xStart+step+1]:
                step += 1
                G_[xStart+step].discard(yStart+step)
            # myG.append([list(range(xStart, xStart+step+1)), list(range(yStart, yStart+step+1)), yStart-xStart])
            # diaGs.append([list(range(xStart, xStart+step+1)), yStart-xStart])
            # diaGs.append([xStart, yStart, yStart-xStart])
            diaGs.append([[xStart, xStart+step+1], step+1])
    diaGs.sort(key=lambda x: x[1]) 
    return diaGs

def remove_node(G, target):
    del G[target]
    for nbrs in G.values():
        nbrs.discard(target)
""" 
def cycles(G, limit):
    def _unblock(thisnode, blocked, B):
            stack = set([thisnode])
            while stack:
                node = stack.pop()
                if node in blocked:
                    blocked.remove(node)
                    stack.update(B[node])
                    B[node].clear()
    G_ = copy.deepcopy(G)
    for startnode in range(nRow):
        path = [startnode]
        blocked = set()  # vertex: blocked from search?
        closed = set()   # nodes involved in a cycle
        blocked.add(startnode)
        B = defaultdict(set)  # graph portions that yield no elementary circuit
        stack = [(startnode,list(G_[startnode]))]
        while stack:
            thisnode, nbrs = stack[-1]
            if nbrs and len(path) <= limit:
                nextnode = nbrs.pop()
                # if len(blocked) > limit:
                #     pass
                if nextnode == startnode:
                    yield path[:]
                    closed.update(path)
                elif nextnode not in blocked:
                    path.append(nextnode)
                    stack.append((nextnode, list(G[nextnode])))
                    closed.discard(nextnode)
                    blocked.add(nextnode)
                    continue
            # done with nextnode... look for more neighbors
            else:
            # if not nbrs or len(path) > limit:  # no more nbrs
                if thisnode in closed:
                    _unblock(thisnode, blocked, B)
                else:
                    if thisnode in G_:
                        for nbr in G_[thisnode]:
                            if thisnode not in B[nbr]:
                                B[nbr].add(thisnode)
                stack.pop()#                assert path[-1] == thisnode
                path.pop()
        # remove_node(G, startnode)
        del G_[startnode]
        for nbrs in G_.values():
            nbrs.discard(startnode) """

mLoad = np.loadtxt('ZTE/Example.csv', dtype=int, delimiter=',')
nRow, nCol = mLoad.shape
# graph adjacency list
GLoad = defaultdict(set)
for i in range(nRow):
    for j in range(nCol):
        if mLoad[i][j] == 1:
            GLoad[i].add(j)
            # GLoad[i].add(j + nRow)
            # GLoad[j + nRow].add(i)
DiaG = g2DiaGs(GLoad, nRow)
print(len(DiaG))




# mLoad2 = np.loadtxt('ZTE/Example_0429.csv', dtype=int, delimiter=',')
# nRow2, nCol2 = mLoad2.shape
# # graph adjacency list
# GLoad2 = defaultdict(set)
# for i in range(nRow2):
#     for j in range(nCol2):
#         if mLoad2[i][j] == 1:
#             GLoad2[i].add(j + nRow2)
#             GLoad2[j + nRow2].add(i)
# DiaG2 = g2DiaGs(GLoad2, nRow2)
# print(len(DiaG2))

# num = [len(n[0]) for n in DiaG]
# nEdge = sum(num)

# num2 = [len(n[0]) for n in DiaG2]
# nEdge2 = sum(num2)

# answer = []
# for i in range(4,15,2):
#     tStart = time.time()
#     cyclesI = []
#     for c in cycles(GLoad, i):
#         if len(c) == i:
#             c.sort()
#             if c not in cyclesI:
#                 cyclesI.append(c)
#     tEnd = time.time()
#     print(len(cyclesI))
#     answer.append(len(cyclesI))
#     print(tEnd - tStart)
# # # distance
# B = [n[2] for n in myG]
# print(max(Counter(B).values()))
# len_ = len(B)
# disNew = defaultdict(list)
# NewX = defaultdict(set)
# NewY = defaultdict(set)
# for i in range(len_):
#     for j in range(i+1,len_):
#         SetX = set(myG[i][0]) & set(myG[j][0])
#         SetY = set(myG[i][1]) & set(myG[j][1])
#         disNew[B[j]-B[i]].append([i,j])
#         NewX[i,j] = SetX
#         NewY[i,j] = SetY
# print(len(NewX))

# for key in disNew.keys():
#     len_ = len(disNew[key])
#     if len_ > 1:
#         for im in range(len_):
#             i = im[0]
#             m = im[1]
#             for jn in range(i+1, len_):
#                 j = jn[0]
#                 n = jn[1]
            #    print(NewY[im] & NewY[jn])





# plt.matshow(d)
# plt.show()


# 三元组，即ijv，记录稀疏矩阵里的非零数据的行i、列j坐标以及值v三个数据。
# adj_coo = ss.coo_matrix(adj_martix)
# adj_dok = ss.dok_matrix(adj_martix)
# adj_lil = ss.lil_matrix(adj_martix)
# adj_dia = ss.dia_matrix(adj_martix)

# for a_1 in range(a):
#     len_ = len(adj_set[a_1])
#     for i in range(len_):
#         for j in range(1+1, len_):
#             cycle_4 = set(adj_set[i]) & set(adj_set[j])