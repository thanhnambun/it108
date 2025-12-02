import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 51, 50)  
y = np.random.randint(0, 51, 50)

plt.scatter(x, y, c='blue')

plt.title("Biểu đồ Scatter của")
plt.xlabel("Trục x")
plt.ylabel("Trục y")

plt.grid(True, linestyle="--")
plt.show()
