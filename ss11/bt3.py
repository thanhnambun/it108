import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)

plt.hist(data, bins=30, color='blue', edgecolor='black')

plt.title("Histogram phân phối chuẩn ")
plt.xlabel("Giá trị")
plt.ylabel("Tần suất xuất hiện")

plt.grid(True, linestyle="--")
plt.show()
