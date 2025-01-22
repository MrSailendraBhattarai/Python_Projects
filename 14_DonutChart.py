
import matplotlib.pyplot as plt

labels=['A','B','C','D','E']
sizes=[30,20,35,15,25]
colors=['red','blue','green','orange','purple']

plt.pie(sizes,labels=labels,colors=colors,wedgeprops={'width':0.4})

centre_circle=plt.Circle((0,0),0.65,color='white',
fc='white',linewidth=1.25)

plt.gca().add_artist(centre_circle)
plt.title("Donut Chart in Python")
plt.show()