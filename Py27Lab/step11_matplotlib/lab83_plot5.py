import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 5)
x2 = np.linspace(0, 2)
x3 = np.linspace(0.1, 10)
print type(x1), len(x1), x1
print type(x2), len(x2), x2
print type(x3), len(x3), x3

y1 = np.cos(2*np.pi*x1)*np.exp(-x1)
y2 = np.cos(np.pi*x2)
y3 = np.tan(x3)*np.log2(x3)

plt.subplot(3,1,1)
plt.plot(x1, y1, 'yo-')

plt.subplot(312)
plt.plot(x2, y2, 'r.-')

plt.subplot(3,1,3)
plt.plot(x3, y3, 'g*-')
plt.show()