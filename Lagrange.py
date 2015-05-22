import numpy as np
from matplotlib.pylab import *

point = []
n = 6
x = arange(0, 5, 0.01)
y = []

def foo(x):
    return 2*sin(2*x) + 1

def getPoint():
    tmpX = [0, 1.5, 2.1, 2.8, 3.9, 4.9]
    for i in tmpX:
        point.append((i, foo(i)))

def Lagrange():
    for i in x:
        s = 0
        for j in range(n):
            p = point[j][1]
            for k in range(n):
                if (j != k):
                    p = p*(i - point[k][0]) / (point[j][0] - point[k][0])
            s += p
        y.append(s)

def drawAll():
    xlim(-0.5, 5.5)
    ylim(-1.1, 5.5)
    title("Lagrange")
    xlabel("x")
    ylabel("y")

    for i in point:
        scatter(i[0], i[1], 25)

    tmp = np.linspace(0, 5, 500)
    plot(tmp, foo(tmp), color="r", label="2*sin(2x)+1")

    plot((x[0], x[1]), (y[0], y[1]), color="c", label="Lagrange")
    legend(loc="upper right")
    for i in arange(0.02, 4.9, 0.005):
        pause(0.0000001)
        j = int(i*100)
        plot((x[j-1], x[j]), (y[j-1], y[j]), color="c")

    savefig("figure/Lagrange.jpg")
    show()

if __name__ == "__main__":
    getPoint()
    Lagrange()
    for i in y:
        print(i)
    drawAll()
    
    
