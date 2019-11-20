import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7,8]
temperature=[50,51,34,134,23,75,2,42]

plt.title("Weather")
plt.xlabel("day")
plt.ylabel("Temperature")
plt.plot(day,temperature,color="red", linewidth='10', linestyle="dotted")
plt.show()



