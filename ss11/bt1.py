import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)

y = x**2 + 2*x

plt.plot(x, y, label="y = x^2 + 2x")

plt.xlabel("Trục x")
plt.ylabel("Trục y")

plt.grid(True, linestyle="--")

plt.legend()
plt.show()
