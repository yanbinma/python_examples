import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider
from MandelbrotSet import MandelbrotSet, drawColorSquares

# user changeable parameters
cur_exp1 = 2

# figure of two subplots: the top one shows the colors used; the bottom one shows the fractal
fig, (ax1, ax2) = plt.subplots(2, gridspec_kw={'height_ratios': [0.1, 0.9]})

# top subplot
drawColorSquares(ax1)

# bottom subplot
plt.title("Mandelbrot Set")
ax2.set_aspect('equal')

def onBoundChange(ax):
    ax.set_autoscale_on(False)
    factal = MandelbrotSet(ax, exp1=cur_exp1)
    factal.draw()
    fig.canvas.draw_idle()

ax2.callbacks.connect('xlim_changed', onBoundChange)
ax2.callbacks.connect('ylim_changed', onBoundChange)
ax2.set_xlim(-2, 2, emit=False)
ax2.set_ylim(-2, 2, emit=True)

# controls
fig.subplots_adjust(bottom=0.25)
axExp1 = fig.add_axes([0.25, 0.1, 0.65, 0.03])
sliderExp1 = Slider(ax=axExp1, label='Exponent1', valmin=2, valmax=100, valinit=2, valstep=1)

def onExp1Changed(val):
    global cur_exp1
    cur_exp1  = val 

sliderExp1.on_changed(onExp1Changed)

axUpdate = fig.add_axes([0.8, 0.025, 0.1, 0.04])
buttonUpdate = Button(axUpdate, 'Update', hovercolor='0.975')

def onUpdate(event):
    ax2.set_xlim(-2, 2, emit=False)
    ax2.set_ylim(-2, 2, emit=True)

buttonUpdate.on_clicked(onUpdate)

axReset = fig.add_axes([0.65, 0.025, 0.1, 0.04])
buttonReset = Button(axReset, 'Reset', hovercolor='0.975')

def onReset(event):
    global cur_exp1
    cur_exp1 = 2
    sliderExp1.set_val(2)
    ax2.set_xlim(-2, 2, emit=False)
    ax2.set_ylim(-2, 2, emit=True)

buttonReset.on_clicked(onReset)
plt.show()
