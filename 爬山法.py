from matplotlib.pylab import *
import numpy as np

#root
def root(x, y):
    return x*x + y*y + 2

#原函数
def f(x, y):
   return 1 / root(x, y)

#一阶偏导
def fxy1(x, y):
    return -2*x / (root(x, y) ** 2)

#一阶偏导平方和
def fxy2(x, y):
    return 4*(x*x + y*y) / (root(x, y) ** 4)

def foo(x, y, z, INIF):
    while (fxy2(x, y) > INIF):
        x, y = x + z*fxy1(x, y), y + z*fxy1(y, x)
        print("x = %.7f, y = %.7f, f = %.3f" % (x, y, f(x, y)))

    return f(x, y)

if __name__ == "__main__":
    """
    x = float(input("x = "))
    y = float(input("y = "))
    z = float(input("z = "))
    """
    print("result = %.7f" % foo(-3.0, 3.0, 0.5, 1e-08))
