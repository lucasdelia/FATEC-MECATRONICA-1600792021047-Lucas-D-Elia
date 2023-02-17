import matplotlib.pyplot as plt
import math 

h = 1
l1 = 1
l2 = 2
theta = 45.0
theta_rad = theta*math.pi/180.0
x0 = 0
y0 = h + l1
x1 = l2*math.cos(theta_rad)
y1 = l2*math.sin(theta_rad) + y0
x2 = 
y2 = 

x = [0, x0, x1]
y = [0, y0, y1]
plt.xlim(-5,5)
plt.ylim(0,5)
plt.plot( x, y)
plt.title("Braco robotico")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(bbox_to_anchor=(0.5,1))
plt.grid(True)

plt.show()
