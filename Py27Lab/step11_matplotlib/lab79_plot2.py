import matplotlib.pyplot as plt
import numpy as np

#x = range(0, 10)
# real number not limited to integer
x = np.arange(0, 10, 0.25)
print x
nx = np.array(x)
ny = nx ** 2
nz = nx ** 2/2
# ro, go, bo
# rs, gs, bs
# r^, g^, b^
# r*, g*, b*
plt.plot(nx, nx, 'r_', nx, ny, 'b*-', nx, nz, 'g^-')
# extra features
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.axis([0, 10, 0, 90])
plt.show()
