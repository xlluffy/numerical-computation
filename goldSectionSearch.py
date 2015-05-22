import numpy as np
from pylab import *

line = []

def drawAll():
    #xlabel("x")
    #ylabel("y = cos(x)")

    x = arange(-pi, pi, 0.01)
    y = cos(x)
    title("Gold Section Search")
    
    xlim(x.min()*1.1, x.max()*1.1)
    ylim(y.min()*1.1, y.max()*1.1)
    xticks(np.linspace(-pi, pi, 5, endpoint=True),
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
    yticks(np.linspace(-1, 1, 3, endpoint=True),
           [r'$-1$', r'$0$', r'$+1$'])

    ax = gca()
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))
    plot(x, y, label="cos(x)")
    legend(loc="upper left")
    
    for i in line:
        pause(0.5)
        plot((i[0],i[0]), (i[1], 0))
    #figtext(0.57, 0.87, "x = %.2f" % line[-1][0])

    scatter(line[-1][0], cos(line[-1][0]), 50, color='blue')
    annotate(r'$\cos(0)=1$',
             xy=(line[-1][0], cos(line[-1][0])), xycoords='data',
             xytext=(+20, +0), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

    savefig("figure/goldSectionSearch.jpg")
    show()

def goldSectionSearch(start, end, INIF):
    x1 = start + 0.382*(end - start)
    x2 = start + 0.618*(end - start)
    f1 = cos(x1)
    f2 = cos(x2)

    global line
    line.append((x1, f1))
    line.append((x2, f2))

    while (end - start > INIF):
        if (f2 > f1):
            start, x1, f1 = x1, x2, f2
            x2 = start + 0.618*(end - start)
            f2 = cos(x2)
            line.append((x2,f2))
        else:
            end, x2, f2 = x2, x1, f1
            x1 = start + 0.382*(end - start)
            f1 = cos(x1)
            line.append((x1,f1))
        print ("start = %.3f, end = %.3f" % (start, end))
        
    return (start + end) / 2

if __name__ == "__main__":
    
    #start = float(input("start: "))
    #end   = float(input("end: "))

    print ("result = %.3f" % goldSectionSearch(-3, 3, 1e-03))
    drawAll()
