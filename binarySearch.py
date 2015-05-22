import numpy as np
from matplotlib.pylab import *

line = []

def setFigure():
    title("x = 2*sin(x)")
    xlabel("x")
    ylabel("y = x - 2*sin(x)")
    axis([-4, 4, -4, 4])
    grid(True)
    
def drawAll(start, end):
    global line
    colorSet = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    index = 0
    line.append((start, end))
    
    for i in line:
        x = arange(i[0], i[1], 0.01)
        y = f(x)
        cla()
        setFigure() 
        plot(x, y, colorSet[index % len(colorSet)], marker='.')
        pause(0.01)
        index += 1
    plot(line[-2][0], f(line[-2][0]), 'ro')
    figtext(0.7, 0.45, 'x = %.3f' % line[-2][0], color = 'y')
    savefig("figure/binarySearch.jpg")
    show()

def f(x):
    return x - 2 * sin(x)

def binarySearch(start, end, INIF):
    global line
    line.append((start, end))
    while (end - start > INIF):
        mid = (start + end) / 2
        if (f(start)*f(mid) < 0):
            end = mid
            line.append((start, mid))
        else:
            start = mid
            line.append((mid, end))
        print ("start = %.3f, end = %.3f, mid = %.3f" % (start, end, mid))
    return (start + end) / 2

if __name__ == "__main__":
    #start = float(input("start: "))
    #end   = float(input("end: "))

    print ("result = %.3f" % binarySearch(-pi, pi, 1e-04))
    drawAll(-pi, pi)
