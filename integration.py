import numpy
from matplotlib.pylab import *

line = []

def f(x):
    if x != 0:
        return sin(x) / x
    else:
        return 0

def Simpson(a, b, e):
    h = b - a
    T0 = h*(f(a) + f(b))/2
    T1 = T0/2 + h*f(a+h/2)
    n = 1

    while(fabs(T1-T0) >= e):
        h /= 2
        n *= 2
        T0, T1 = T1, 0
        x, fx = 0, 0
        for k in range(1, n+1):
            x = a + (k-1/2)*h
            fx = f(x)
            T1 += fx
            line.append(((x,0), (x,fx)))
        T1 = T0/2 + h*T1/2
    return T1

def drawAll():
    xlim(0, 7)
    ylim(-0.5, 1)
    xlabel("x")
    ylabel("y")
    title("integration")

    x = np.linspace(0, 7, 600)
    plot(x, sin(x)/x, "r")
    for i in line:
        pause(0.00000001)
        plot((i[0][0], i[1][0]), (i[0][1], i[1][1]))

    savefig("figure/integration.jpg")
    show()

if __name__ == "__main__":
    """
    a = float(input("a = "))
    b = float(input("b = "))
    e = float(input("e = "))
    """
    print("result = %.3f" % Simpson(0.0, 6.0, 1e-04))
    print(len(line))
    drawAll()
    show()
