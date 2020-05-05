import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection

mLoad = np.loadtxt('ZTE5/Example_0429.csv', dtype=int, delimiter=',')
nRow, nCol = mLoad.shape

fig1 = plt.figure()
ax1 = fig1.add_subplot()
ax1.matshow(mLoad)
plt.grid(color='black', linestyle='-', linewidth=0.5)
xticks = np.arange(0, nCol, step=64)
yticks = np.arange(0, nRow, step=64)
plt.xticks(xticks)#,fontsize=3)
plt.yticks(yticks)#,fontsize=3)


# #128,414,211,811/128,211,414,811
# rect1 = plt.Rectangle((414-nRow, 128),811-414,211-128,
#                         fill=False, edgecolor = 'red',linewidth=2)
# ax1.add_patch(rect1)
# #161,447,244,780/161,244,447,780
# rect1 = plt.Rectangle((447-nRow, 161),780-447,244-161,
#                         fill=False, edgecolor = 'red',linewidth=2)
# ax1.add_patch(rect1)

# #162,781,245,384/162,245,384,781
# rect2 = plt.Rectangle((384-nRow, 162),781-384,245-162,
#                         fill=False, edgecolor = 'green',linewidth=2)
# ax1.add_patch(rect2)
# #172,255,394,791
# rect2 = plt.Rectangle((394-nRow, 172),791-394,255-172,
#                         fill=False, edgecolor = 'green',linewidth=2)
# ax1.add_patch(rect2)

# #173,192,395,792
# rect3 = plt.Rectangle((395-nRow, 173),792-395,192-173,
#                         fill=False, edgecolor = 'blue',linewidth=2)
# ax1.add_patch(rect3)
# #191,413,210,810/191,210,413,810
# rect3 = plt.Rectangle((413-nRow, 191),810-413,210-191,
#                         fill=False, edgecolor = 'blue',linewidth=2)
# ax1.add_patch(rect3)

patches = []

# path = [0,639,136,352,208,682]
path = [0,639,136,422,12,587,238,740]
for i in range(len(path)):
    if i % 2 == 1:
        path[i] = path[i] - nRow
path.append(path[0])

points = []
for i in range(len(path)-1):
    if i % 2 == 0:
        points.append([path[i+1], path[i]])
    else:
        points.append([path[i], path[i+1]])

# polygon = Polygon(points, True)
polygon = plt.Polygon(points, fill=None, edgecolor='r')
plt.gca().add_line(polygon)
# patches.append(line)
# colors = 100*np.random.rand(len(patches))
# p = PatchCollection(patches, alpha=0.4)
# p.set_array(np.array(colors))
# ax1.add_collection(p)
plt.show()