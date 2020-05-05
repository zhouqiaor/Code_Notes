import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mLoad = np.loadtxt('ZTE5/Example_0430.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    G0 = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                G0[i].add(j + nRow)
                G0[j + nRow].add(i)
    # print(G0[0])
    L = list(np.array(list(G0[0])) - nRow)
    L.sort()
    # [50, 293, 574, 899, 1060, 1319]
    B = [i*192 for i in range(nRow//192 + 1)]
    # [0, 192, 384, 576, 768, 960, 1152, 1344]
    # mNew = mLoad[:][:]
    mNp = np.matrix(mLoad)
    # mNew = np.zeros((nRow, nCol))
    mNew = np.hstack((mNp[:,50:192],mNp[:,0:50],#0, 192
                      mNp[:,293:384],mNp[:,192:293],#192, 384
                      mNp[:,574:576],mNp[:,384:574],#384, 576
                      mNp[:,576:768],#576, 768
                      mNp[:,899:960],mNp[:,768:899],#768, 960
                      mNp[:,1060:1152],mNp[:,960:1060],#960, 1152
                      mNp[:,1319:1344],mNp[:,1152:1319]))#1152, 1344
    plt.matshow(mNp)
    plt.grid(color='g', linestyle='-', linewidth=0.5)
    xticks = np.arange(0, nCol, step=192)
    yticks = np.arange(0, nRow, step=192)
    plt.xticks(xticks)#,fontsize=3)
    plt.yticks(yticks)#,fontsize=3)
    plt.savefig('ZTE5/mNp_0430.png', dpi=800)
    # plt.show()