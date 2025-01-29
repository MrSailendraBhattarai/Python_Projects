
# Pie chart

import matplotlib.pyplot as pyplot

labels=('Python','Java','C','C++')
sizes=[45,20,15,20]

pyplot.pie(sizes,labels=labels,autopct='%1.f%%',
        counterclock=False,startangle=105)

pyplot.show()