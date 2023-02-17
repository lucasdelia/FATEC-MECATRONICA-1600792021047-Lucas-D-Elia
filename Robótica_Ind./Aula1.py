import matplotlib.pyplot as plt

x = [0,5,10]
y1 = [0,5,5]
y2 = [0,3,10]

plt.plot(x, y1, label = "linha1")
plt.plot(x, y2, label = "linha2")

plt.title("Branco robotico")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
