import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

plt.plot(x, y, label="y = sin(x)", color="blue")

x_point = np.pi / 2
y_point = np.sin(x_point)

plt.scatter(x_point, y_point, color="red")

plt.annotate(
    "Đỉnh sóng tại x = π/2",          
    xy=(x_point, y_point),             
    xytext=(x_point + 0.5, y_point + 0.3),
    arrowprops=dict(arrowstyle="->", color="red"),
    fontsize=10
)

plt.title("Đồ thị hàm sin ")
plt.xlabel("x")
plt.ylabel("sin(x)")

plt.grid(True, linestyle="--")
plt.legend()

plt.show()
