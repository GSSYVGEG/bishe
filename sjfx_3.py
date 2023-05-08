import matplotlib.pyplot as plt
import linecache
import matplotlib.animation as animation
import math

# 动画
g_files = ["ljx-gaipian-2.igtif"]

g_pointSize = 1  # 点的尺寸大小
g_ylist_lineNumBegin = 15
g_ylist_lineNumEnd = 600

g_yMax = 0.8 # y轴坐标最大值
g_yMin = -0.8 # y轴坐标最小值

temp_title = ""
for fileName in g_files:
    temp_title += " "
    temp_title += fileName


def getXList(file):
    with open(file,'r',encoding='utf-8') as f:
        for line in f:
            if line.startswith('#properties'):
                line = line.replace("#properties ","")
                xList = [float(x) for x in line.split()]
                return xList


def getYList(file, lineNum):
    line = linecache.getline(file, lineNum)
    valueList = [float(x) for x in line.split()]
    return valueList[3:]


def drawScatter(file, lineNum):
    xList = getXList(file)
    yList = getYList(file, lineNum)
    # print("------"+str(len(xList)),"---",str(len(yList)))
    # 绘制散点图
    plt.scatter(xList, yList, g_pointSize)
    return min(yList), max(yList)


n_frames = g_ylist_lineNumEnd-g_ylist_lineNumBegin
fig, ax = plt.subplots()


def update(frame):
    ax.clear()
    for file in g_files:
        drawScatter(file, frame+g_ylist_lineNumBegin)
    ax.set_ylim(g_yMin,g_yMax)
    # 添加标题和标签
    ax.set_title(temp_title+" / line " + str(frame+g_ylist_lineNumBegin))
    ax.set_xlabel("Time[ps]")
    ax.set_ylabel("Amplitude[a.u.]")
    return ax


ani = animation.FuncAnimation(fig, update, frames=n_frames, interval=100)
ani.save("out/"+g_files[0]+".gif", writer='pillow')
