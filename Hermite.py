__author__ = 'xlluffy'
import numpy as np
from matplotlib.pylab import *

point = []
#point = [(0, 1), (1, 2), (3, 4), (4, 5), (5, 6), (6, 7)]
n = 5
x = arange(0, 5, 0.01)
y, a, b, c, d, h, s  = [], [], [], [], [], [], []

def foo(x):
    return 2*sin(2*x) + 1

def getPoint():
    tmpX = [0, 1.5, 2.1, 2.8, 3.9, 4.9]
    for i in tmpX:
        point.append((i, foo(i)))

def init():
    for i in range(n+1):
        a.append(0)
        b.append(0)
        c.append(0)
        d.append(0)
        h.append(0)
        s.append(0)

def Hermite():
    init()
    for i in range(n):
        h[i] = point[i+1][0] - point[i][0]

    a[1] = 2*(h[0] + h[1])
    for i in range(2, n):
        a[i] = 2*(h[i-1] + h[i]) - h[i-1]*h[i-1]/a[i-1]

    for i in range(1, n+1):
        c[i] = (point[i][1] - point[i-1][1]) / h[i-1]

    for i in range(1, n):
        d[i] = 6*(c[i+1] - c[i])

    b[1] = d[1]
    for i in range(2, n):
        b[i] = d[i] - b[i-1]*h[i-1]/a[i]

    s[n-1] = b[n-1]/a[n-1]
    for i in range(n-2, 0, -1):
        s[i] = (b[i] - h[i]*s[i+1])/a[i]

    for i in range(n):
        for j in arange(point[i][0], point[i+1][0], 0.01):
            S1 = c[i+1] - s[i+1]*h[i]/6 - s[i]*h[i]/3
            tmp  = point[i][1] + S1*(j-point[i][0]) + s[i]*((j-point[i][0])**2)/2 + (s[i+1] - s[i])*((j - point[i][0])**3)/(6*h[i])
            y.append(tmp)

def drawAll():
    xlim(-0.5, 5.3)
    ylim(-5, 8.5)
    xlabel("x")
    ylabel("y")
    title("Hermite")

    for i in point:
        scatter(i[0], i[1], 25)

    tmp = np.linspace(0, 5, 500)
    plot(tmp, foo(tmp), color="r", label="2*sin(2x)+1")

    plot((x[0], x[1]), (y[0], y[1]), color="c", label="Hermite")
    legend(loc="upper right")
    for i in arange(0.01, 4.9, 0.005):
        #pause(0.0001)
        j = int(i*100)
        plot((x[j-1], x[j]), (y[j-1], y[j]), color="c")
    savefig("figure/Hermite.jpg")
    show()

if __name__ == "__main__":
    getPoint()
    Hermite()
    for i in y:
        print(i)
    drawAll()