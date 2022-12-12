import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir(r'E:\BS Teaching\Fall2022\IDS\PyProgs\CSV_Files')
data = pd.read_csv("LinearRegression.csv")
print(data.head())
x_val = data['x']
y_val = data['y']


#plt.style.use("ggplot")
fig = plt.figure()
ax = fig.add_subplot() # Row Col Number
plt.scatter(x_val, y_val, color ='green')
plt.show()
# plt.scatter(x_val, y_val, color ='green', s=y_val) # Size
# plt.scatter(x_val, y_val, color ='green', marker='*') # marker [*,d,s,<,>]
# plt.scatter(x_val, y_val, color ='green', alpha=0.2) # Transparency

# ax.set_xlabel('Age')
# ax.set_ylabel('Salary ')
# plt.title('X Y Scatter Plot', color = 'g')

#
# ax.xaxis.label.set_color('red')    #setting up X-axis label color
# ax.yaxis.label.set_color('blue')   #setting up Y-axis label color
#
# ax.tick_params(axis='x', colors='blue')    #setting up X-axis tick color
# ax.tick_params(axis='y', colors='red')  #setting up Y-axis tick color

# ax.spines['left'].set_color('red')
# ax.spines['top'].set_color('red')
# ax.spines['right'].set_color('blue')
# ax.spines['bottom'].set_color('blue')

# plt.xlim([1, 35])
# plt.ylim([100, 700])

# plt.grid(b=True, which='major', color='b', linestyle='-')
# plt.grid(b=True, which='minor', color='r', linestyle='-')
# plt.show()

# plt.scatter(x_val, y_val, color ='green')
# plt.legend(['Data Points'], loc = 'upper left')
# plt.show()


