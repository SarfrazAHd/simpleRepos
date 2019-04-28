import matplotlib.pyplot as plt

day=[1,2,3,4,5,6,7]
min_temp=[43,42,40,44,33,35,37]
avg_temp=[45, 48,48,46,48,42,41]
max_temp=[38,51,52,48,47,49,46]

plt.title("Weather")
plt.xlabel("Day")
plt.ylabel("Temperature")

plt.plot(day, min_temp, label="Minimum")
plt.plot(day, avg_temp, label="Average")
plt.plot(day, max_temp, label="Maximum")
#plt.legend()
#plt.legend(loc="lower right")
#plt.legend(loc="center")
plt.legend(loc="lower left", shadow=True, fontsize="large")


plt.grid()
plt.show()