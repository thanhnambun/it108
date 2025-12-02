import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

x = np.linspace(0, 2*np.pi, 200)
line, = ax.plot(x, np.sin(x))

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel("Trục x")
ax.set_ylabel("Trục y")
ax.set_title("Đồ thị động: y = sin(x)")

def update(frame):
    y = np.sin(x + frame * 0.1)   
    line.set_ydata(y)
    return line,

ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

plt.show()
