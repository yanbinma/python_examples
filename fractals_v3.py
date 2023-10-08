import numpy as np
import matplotlib.pyplot as plt

#v3 focuses on the effects with changing exponent values for both Z and C
num=200
tests=125
exp1=2
exp2=1
# test 'tests' times, starting from 0 
def isMandelbrotSet(cn):
    z = 0
    for i in range(tests):
        z = z**exp1 + cn**exp2
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

# test all complex numbers within (-2:2, -2:2)
plt.ion()
for exp1 in range(2, 100):
    for exp2 in range(1,10):
        plt.clf()
        drawInRect(-2, 2, -2, 2)
        plt.title("Mandelbrot Exponents: " + str(exp1) + ", " + str(exp2))
        plt.gcf().canvas.draw()
        plt.gcf().canvas.flush_events()
        plt.pause(1)
