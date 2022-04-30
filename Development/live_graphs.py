# four live updating subplots
import random as r
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

x1_values = []
y1_values = []

x2_values = []
y2_values = []

x3_values = []
y3_values = []

x4_values = []
y4_values = []

index1 = count()
index2 = count()
index3 = count()
index4 = count()


def animate(i):
    x1_values.append(next(index1))
    y1_values.append(r.randint(0, 5))

    x = np.array(x1_values)
    y = np.array(y1_values)
    plt.subplot(2, 2, 1)
    plt.cla()
    plt.plot(x, y)

    plt.xlabel('Time (s)')
    plt.ylabel('Value1')
    plt.title('Value1 vs. Time')

    x2_values.append(next(index2))
    y2_values.append(r.randint(0, 5))

    x = np.array(x2_values)
    y = np.array(y2_values)
    plt.subplot(2, 2, 2)
    plt.cla()
    plt.plot(x, y)

    plt.xlabel('Time (s)')
    plt.ylabel('Value2')
    plt.title('Value2 vs. Time')

    x3_values.append(next(index3))
    y3_values.append(r.randint(0, 5))

    x = np.array(x3_values)
    y = np.array(y3_values)
    plt.subplot(2, 2, 3)
    plt.cla()
    plt.plot(x, y)

    plt.xlabel('Time (s)')
    plt.ylabel('Value3')
    plt.title('Value3 vs. Time')

    x4_values.append(next(index4))
    y4_values.append(r.randint(0, 5))

    x = np.array(x4_values)
    y = np.array(y4_values)
    plt.subplot(2, 2, 4)
    plt.cla()
    plt.tight_layout()
    plt.plot(x, y)

    plt.xlabel('Time (s)')
    plt.ylabel('Value4')
    plt.title('Value4 vs. Time')


ani = FuncAnimation(plt.gcf(), animate, 1000)

plt.suptitle('Values vs. Time Data')
plt.show()
