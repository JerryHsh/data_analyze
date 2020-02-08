import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[value**2 for value in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolors='none',s=10)


#set chart title and label axes
plt.title("square number",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
#set the size of the tick labels
plt.tick_params(axis='both',which='major',labelsize=14)

#set the range of each axies
plt.axis([0,1100,0,1100000])

plt.show()