import numpy as np
import scipy.integrate as inte
from matplotlib.pylab import *

line = []
ST = [0]
a, b = 0, 0

def f(x):
    if x != 0:
        return sin(x) / x
    else:
        return 0

def Simpson(a, b, e):
    for i in range(100):
        ST.append(0)
    e /= b - a
    i, s, u, v = 0, 0, a, b
    flag = 1
    while flag == 1:
        h  = v - u
        T1 = (f(u) + f(v)) * h/2
        w  = (u + v) / 2
        T2 = T1/2 + h*f(w)/2

        line.append([(w,0),(w,f(w))])

        if fabs(T2 - T1) >= (e*h):
            i += 1
            ST[i] = v
            v = w
            flag = 1
        else:
            flag = 0
            s += T2
            if i != 0:
                u = v
                v = ST[i]
                i -= 1
                flag = 1
    return s

def drawAll():
    xlim(0, 7)
    ylim(-0.5, 1)
    xlabel("x")
    ylabel("y")
    title("Simpson")

    ax = gca()
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    x = np.linspace(0, 7, 600)
    y = sin(x)/x
    plot(x, y, "r", label="sin(x)/x")
    legend(loc="upper right")
    for i in line:
        pause(0.00001)
        plot((i[0][0], i[1][0]), (i[0][1], i[1][1]))

    savefig("figure/Simpson.jpg")

if __name__ == "__main__":
    """
    a = float(input("a = "))
    b = float(input("b = "))"""

    Simpson(1.0, 6.0, 1e-4)
    print(len(line))
    #print("result = %.3f" % Simpson(1, 6, 1e-4))
    #print("result - %.3f" % inte.quad(lambda x:sin(x)/x, 1, 6))
    drawAll()
    show()
