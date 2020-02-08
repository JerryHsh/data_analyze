import matplotlib.pyplot as plt
#when you give plot a series of number it assume that the first x-value is 0 
#to change the situation we give plot the input value
input_value=[1,2,3,4,5]
squares=[1,4,9,16,25]
plt.plot(input_value,squares,linewidth=5)

plt.title("Squares number",fontsize=24)
plt.xlabel("value",fontsize=14)
plt.ylabel("square of value",fontsize=14)
plt.show()