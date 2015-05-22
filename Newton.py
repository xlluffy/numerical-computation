__author__ = 'xlluffy'
import numpy as np
from matplotlib.pylab import *

point = []
n = 6
x = arange(0, 5.0, 0.01)
a, y = [], []

def foo(x):
    return 2*sin(2*x) + 1

def getPoint():
    tmpX = [0, 1.5, 2.1, 2.8, 3.9, 4.9]
    for i in tmpX:
        point.append((i, foo(i)))

#获取系数
def getCoefficient():
    for i in point:
        a.append(i[1])

    for i in range(1, n):
        for j in range(n-1, i-1, -1):
            a[j] = (a[j]-a[j-1]) / (point[j][0] - point[j-i][0])

def Newton():
    getCoefficient()

    for i in x:
        p = a[-1]
        for j in range(n-1, -1, -1):
            p  = p*(i - point[j][0]) + a[j]
        y.append(p)

def drawAll():
    xlim(-0.5, 5.5)
    ylim(-1.1, 4)
    xlabel("x")
    ylabel("y")
    title("Newton")

    for i in point:
        scatter(i[0], i[1], 25)

    tmp = np.linspace(0, 5, 500)
    plot(tmp, foo(tmp), color="r", label="2*sin(2x)+1")

    plot((x[0], x[1]), (y[0], y[1]), color="c", label="Lagrange")
    legend(loc="upper right")
    for i in arange(0.02, 4.9, 0.005):
        #pause(0.0000001)
        j = int(i*100)
        plot((x[j-1], x[j]), (y[j-1], y[j]), color="c")
    savefig("figure/Newton.jpg")
    show()

if __name__ == "__main__":
    getPoint()
    Newton()

    for i in y:
        print(i)

    drawAll()

