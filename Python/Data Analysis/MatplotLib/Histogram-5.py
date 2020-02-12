import matplotlib.pyplot as plt

blood_pressure_men=[124,24,53,254,54,80,98,134,324]
blood_pressure_women=[84,14,33,234,34,70,102,234,304]
blood_pressure_kids=[10,24,34,54,12,51,42,54,65,76]

plt.title("Blood Pressure Analysis")
plt.xlabel("Sugar Range")
plt.ylabel("Frequency Range")
plt.hist([blood_pressure_men, blood_pressure_women, blood_pressure_kids], bins=4, rwidth=0.75, color=['green', 'orange', 'blue'], 
label=["Men", "Women", "kids"])
plt.legend()
plt.show()
