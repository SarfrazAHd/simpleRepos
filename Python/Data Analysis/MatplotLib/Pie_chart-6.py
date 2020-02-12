import matplotlib.pyplot as plt


plt.title("Pie Chart", color="green")
labels = 'Room rent', 'food', 'Trassport', 'others','mobile'
expanses = [3500, 2500, 1000,300,500]
explode = (0.1, 0.2, 0, 0,0)  

plt.pie(expanses, labels=labels, shadow=True,autopct='%1.1f%%',)
plt.axis('equal') 
plt.show()