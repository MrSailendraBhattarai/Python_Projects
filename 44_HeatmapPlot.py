
# HeatMap plot

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import random

data=np.random.rand(10,12)
sns.heatmap(data,cmap='Reds')
plt.show()

