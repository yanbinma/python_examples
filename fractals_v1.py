import numpy as np
import matplotlib.pyplot as plt

num=200
# one interesting find: the resulted shape seems to be power-1 sided;
# when power=6, it's shaped as a pentagon; when zoom-in, it starts to look like human palm with 5 fingers 
power=6
tests=125
toShow=False
# test 'tests' times, starting from 0 
def isMandelbrotSet(cn):
    z = 0
    for i in range(tests):
        z = z**power + cn
        if abs(z.real)>2.0 or abs(z.imag)>2.0:
            return False
    return True

# given a rectangle, draw in the area
def calcCoordinatesInRect(x1,x2,y1,y2):
    xlist=[]
    ylist=[]
    A=np.linspace(x1, x2, num)
    B=np.linspace(y1, y2, num)
    for x in range(0, num):
        for y in range(0, num):
            if isMandelbrotSet(complex(A[x],B[y])):
                xlist.append(A[x])
                ylist.append(B[y])
    return xlist, ylist                

def drawInRect(x1,x2,y1,y2):
    xlist, ylist = calcCoordinatesInRect(x1,x2,y1,y2)
    plt.scatter(xlist, ylist)
    if toShow:
        plt.show()

# test all complex numbers within (-2:2, -2:2)

def onBoundChange(ax):
    ax.set_autoscale_on(False)
    vl = ax.viewLim
    drawInRect(vl.x0,vl.x1,vl.y0,vl.y1)

ax=plt.gca()
ax.callbacks.connect('xlim_changed', onBoundChange)
ax.callbacks.connect('ylim_changed', onBoundChange)

plt.title("Mandelbrot Set")
ax.set_xlim([-2,1])
ax.set_ylim([-1,1])
toShow=True
onBoundChange(ax)

