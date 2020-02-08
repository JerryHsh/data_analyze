import matplotlib.pyplot as plt

x_values=list(range(1,5001))
y_values=[value**3 for value in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=10)

plt.title("cube number",fontsize=24)
plt.xlabel("x value",fontsize=14)
plt.ylabel("y value",fontsize=14)
plt.show()