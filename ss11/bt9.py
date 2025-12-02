import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

days = 30
dates = [dt.date(2024, 1, 1) + dt.timedelta(days=i) for i in range(days)]

np.random.seed(42)
temps = np.random.normal(25, 3, days)

temps[5] += 6
temps[15] -= 5
temps[25] += 7

x = np.arange(days)
trend = np.poly1d(np.polyfit(x, temps, 1))(x)

special_dates = [5, 15, 25] 
special_labels = ["Nóng đột biến", "Lạnh bất thường", "Siêu nóng"]

plt.figure(figsize=(12, 6))
plt.plot(dates, temps, label="Nhiệt độ thực tế", marker='o', linewidth=2)

plt.plot(dates, trend, color='red', linestyle='--', label="Trendline")

plt.scatter([dates[i] for i in special_dates],
            [temps[i] for i in special_dates],
            color="orange", s=100, zorder=5, label="Spikes")

for i, label in zip(special_dates, special_labels):
    plt.annotate(label,
                 xy=(dates[i], temps[i]),
                 xytext=(dates[i] + dt.timedelta(days=1), temps[i] + 1),
                 arrowprops=dict(arrowstyle="->", color="orange"))

plt.title("Chuỗi thời gian nhiệt độ trong tháng của Hải Anh xinh gái")
plt.xlabel("Ngày")
plt.ylabel("Nhiệt độ (°C)")
plt.grid(True, linestyle="--")
plt.xticks(rotation=45)
plt.legend()

plt.tight_layout()
plt.show()
