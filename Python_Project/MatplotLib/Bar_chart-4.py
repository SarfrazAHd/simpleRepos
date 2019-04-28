import matplotlib.pyplot as plt
import numpy as np

company=["Google","Facebook","Amazon", "Microsoft"]
revenue=[13,16,27,38]
Profit=[5, 9, 14,20]


x=np.arange(len(company))

plt.title("US Text stock", color="red")

plt.xlabel("Company Name", color="brown")

plt.ylabel("Annual Revenue", color="brown")

plt.bar(x-0.2, revenue,  label="Revenue", width=0.4)
plt.bar(x+0.2, Profit,  label="Profit", width=0.4)

# Horizontal Plot 
#plt.barh(x-0.2, revenue,  label="Revenue")

#plt.barh(x+0.2, Profit,  label="Profit")

plt.legend()
plt.show()