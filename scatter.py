import matplotlib.pyplot as plt

x_values=list(range(1,1001))
y_values=[value**2 for value in x_values]
#the point's original color is blue and it has the outlines which is black 
#to remove it use edgecolor='none'
#to change the points color use c= both rgb tutle(value closer to 0 produce darker color and value closer to 1 produce lighter color) 
# and the color name string is ok
plt.scatter(x_values,y_values,c=(0,0,0.8),edgecolors='none',s=10)
#set chart title and label axes
plt.title("square number",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
#set the size of the tick labels
plt.tick_params(axis='both',which='major',labelsize=14)

#set the range of each axies
plt.axis([0,1100,0,1100000])

plt.show()