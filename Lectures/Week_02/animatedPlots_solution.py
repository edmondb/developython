#!/usr/bin/env python

"""
   NASA Langley Research Center
   Fall 2016 Python Training

        BREAKOUT SOLUTION
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random


N = 200
a = -2.0
b = 3.0

#---------------------------
# Set up figure for plotting
#---------------------------
fig = plt.figure()
ax = fig.add_subplot(111)
line, = ax.plot([], [], 'bo', ms=4)
ax.set_xlim(a, b)
ax.set_ylim(-1.05, 1.05)
ax.set_xlabel('x')
ax.set_ylabel('$y = \sin(\pi x)$')


def update():
    x = np.zeros(N)
    for i in range(N):
        x[i] = random.uniform(a,b)
    x = np.sort(x)
    y = np.sin(np.pi*x)
    yield x, y

def draw(data):
    line.set_xdata(data[0])
    line.set_ydata(data[1])
    return line,

ani = animation.FuncAnimation(fig, draw, update, interval=1000, blit=False)

plt.show()
