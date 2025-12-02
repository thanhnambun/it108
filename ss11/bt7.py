import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = np.random.randint(0, 100, (10, 10))

plt.figure(figsize=(8, 6))
sns.heatmap(data, 
            cmap="viridis",   
            annot=True,        
            fmt="d",       
            linewidths=0.5,    
            cbar=True)  

plt.title("Heatmap 10x10 ", fontsize=14)
plt.xlabel("Cột")
plt.ylabel("Hàng")

plt.show()
