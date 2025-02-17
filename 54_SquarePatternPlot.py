
# Square Pattern Plot

import matplotlib.pyplot as plt

n=4
plt.figure(figsize=(5,5))

for i in range(n):
    for j in range(n):
        plt.scatter(j,-i,s=500,c='red')

plt.axis('off')
plt.gca().set_aspect('equal',adjustable='box')
plt.title('Square Pattern Plot', fontsize=14)

plt.show()