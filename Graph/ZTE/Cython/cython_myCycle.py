import numpy as np
import myCycle
from collections import Counter
from collections import defaultdict
# python myCycle_setup.py build_ext --inplace

if __name__ == '__main__':
    mLoad = np.loadtxt('/Users/z/Desktop/Code_Notes/Graph/ZTE/Example_0501.csv', dtype=int, delimiter=',')
    nRow, nCol = mLoad.shape
    GLoad = defaultdict(set)
    for i in range(nRow):
        for j in range(nCol):
            if mLoad[i][j] == 1:
                GLoad[i].add(j + nRow)
                GLoad[j + nRow].add(i)
    for num in [4, 6, 8, 10, 12, 14]:
        Cs = myCycle.myCycle(GLoad, range(nRow), num)
        print(num, len(Cs))
    # len_cs = [len(c) for c in Cs]
    # result = Counter(len_cs)
    # print(result)