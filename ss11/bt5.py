import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y1 = x
y2 = x**2

x_rand = np.random.randint(0, 50, 50)
y_rand = np.random.randint(0, 50, 50)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, y1, color='red')
axs[0, 0].set_title("Đồ thị y = x")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("y")
axs[0, 0].grid(True, linestyle="--")

axs[0, 1].plot(x, y2, color='green')
axs[0, 1].set_title("Đồ thị y = x²")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("y")
axs[0, 1].grid(True, linestyle="--")

axs[1, 0].scatter(x_rand, y_rand, color='blue')
axs[1, 0].set_title("Scatter ngẫu nhiên")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("y")
axs[1, 0].grid(True, linestyle="--")

axs[1, 1].scatter(np.random.randn(50), np.random.randn(50), color='purple')
axs[1, 1].set_title("Scatter phân phối chuẩn")
axs[1, 1].set_xlabel("x")
axs[1, 1].set_ylabel("y")
axs[1, 1].grid(True, linestyle="--")

plt.tight_layout()
plt.show()
