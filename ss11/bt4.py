import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

y1 = x
y2 = x**2
y3 = x**3

plt.plot(x, y1, color='red', label='y = x')
plt.plot(x, y2, color='green', label='y = x^2')
plt.plot(x, y3, color='blue', label='y = x^3')

plt.title("Ba đường hàm số của")
plt.xlabel("Trục x")
plt.ylabel("Trục y")

plt.legend()

plt.grid(True, linestyle='--')

plt.show()
