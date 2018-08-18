import matplotlib.pyplot as plt
import numpy as np

#r1 = np.arange(-2, 2, 0.1)
r1 = np.linspace(0, 100)
print type(r1), len(r1), r1
plt.plot(r1, r1**2, 'gs')
plt.show()
