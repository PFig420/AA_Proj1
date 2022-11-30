# importing package
import matplotlib.pyplot as plt
  
# create data
x = [4,5,6,8,10,15,20]


basic_ops_125_ex = [1,2,2,4,6,14,24]
basic_ops_25_ex = [2,3,4,7,12,27,48]
basic_ops_50_ex = [3,5,8,14,23,53,95]
basic_ops_75_ex = [5,8,12,21,34,79,143]
basic_ops_125_g = [4,5,6,8,10,15,20]
basic_ops_25_g = [4,5,6,8,10,15,20]
basic_ops_50_g = [4,5,6,8,10,15,20]
basic_ops_75_g = [4,5,6,8,10,15,20]
  
# plot lines
plt.plot(x, basic_ops_125_ex, label = "125_ex", color = "red")
plt.plot(x, basic_ops_125_g,label = "125_g", color = "blue")
plt.plot(x, basic_ops_25_ex, label = "25_ex", color = "green")
plt.plot(x, basic_ops_25_g,label = "25_g", color = "brown")
plt.plot(x, basic_ops_50_ex, label = "50_ex", color = "pink")
plt.plot(x, basic_ops_50_g,label = "50_g", color = "black")
plt.plot(x, basic_ops_75_ex, label = "75_ex", color = "yellow")
plt.plot(x, basic_ops_75_g,label = "75_g", color = "orange")
plt.legend()
plt.show()