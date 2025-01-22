
# pip install matplotlib
# Colored Bar Graph
import matplotlib.pyplot as plt
categories=['A','B','C','D','E']
values=[10,15,7,12,20]
colors=['red','blue','green','orange','purple']

plt.bar(categories,values,color=colors)

plt.xlabel('categories')
plt.ylabel('values')
plt.title("Colored Bar Graph")

plt.show()