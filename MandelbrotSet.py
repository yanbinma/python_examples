import numpy as np
import matplotlib.pyplot as plt

DEFAULT_NUM_OF_PIXELS=150
DEFAULT_EXPONENT_1=2
DEFAULT_EXPONENT_2=1
DEFAULT_NUM_OF_TESTS=125

# rainbow colors
rainbow_colors = ['#0000FF', '#00FF00', '#FFFF00', '#FF7F00', '#FF2600', '#FF3500', '#FF4000', '#ff5100', '#ffac00', '#fff100', '#0bff00', '#00f6ff', '#233067']
#rainbow_colors = ['#0000FF', '#007F7F', '#55AAAA', '#00FF00', '#7FFF00', '#AAFF55', '#FFFF00', '#FFBF00', '#FFD455', '#FF7F00', '#FF5200', '#FF8C55', '#FF2600', '#FF2D00', '#FF7355', '#FF3500', '#FF3A00', '#FF7C55', '#FF4000', '#FF4800', '#FF8555', '#ff5100', '#FF7E00', '#FFA955', '#ffac00', '#FFCE00', '#FFDE55', '#fff100', '#85F800', '#ADFA55', '#0bff00', '#05FA7F', '#58FCAA', '#00f6ff', '#1193B3', '#60B7CC', '#233067']  

class MandelbrotSet: 
    def __init__(self, ax, nPixels=DEFAULT_NUM_OF_PIXELS, exp1=DEFAULT_EXPONENT_1, exp2=DEFAULT_EXPONENT_2, nTests=DEFAULT_NUM_OF_TESTS) -> None:
        self._ax = ax
        self._nPixels = nPixels
        self._exp1 = exp1
        self._exp2 = exp2
        self._nTests = nTests
        self._cfactor = np.ceil(nTests * 1.0 / len(rainbow_colors))
        vl=ax.viewLim
        self._xlist, self._ylist, self._clist=self.calcCoordinatesInRect(vl.x0,vl.x1,vl.y0,vl.y1)

    def evalComplexNumber(self, cn):
        z = 0
        for i in range(self._nTests):
            z = z**self._exp1 + cn**self._exp2
            if abs(z.real)>2.0 or abs(z.imag)>2.0:
                return i
        return 0

    # given a rectangle, draw in the area
    def calcCoordinatesInRect(self, x1,x2,y1,y2):
        xlist=[]
        ylist=[]
        clist=[]
        A=np.linspace(x1, x2, self._nPixels)
        B=np.linspace(y1, y2, self._nPixels)
        for x in range(0, self._nPixels):
            for y in range(0, self._nPixels):
                ccode = self.evalComplexNumber(complex(A[x],B[y]))
                xlist.append(A[x])
                ylist.append(B[y])
                clist.append(ccode % self._cfactor)
        return xlist, ylist, clist  
    
            
    def draw(self):
        self._ax.scatter(self._xlist, self._ylist, c=self._clist)

def drawColorSquares(ax):
    ax.set_xlim([0, len(rainbow_colors)])
    ax.set_ylim([0,1])
    ax.axis('off')
    for i in range(len(rainbow_colors)):
        ax.add_patch(plt.Rectangle((i,0), 1, 1, color=rainbow_colors[i]))

