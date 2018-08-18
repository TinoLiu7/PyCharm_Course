startRange1 = range(0, 20)
print type(startRange1), startRange1
startRange2 = range(0, 20, 2)
print startRange2
startRange3 = range(20, 0, -1)
print startRange3

# from int to float
import numpy as np

startRange4 = np.arange(0, 20)
print type(startRange4), startRange4
startRange5 = np.arange(0, np.pi)
print startRange5
startRange6 = np.arange(0, np.pi, 0.1)
print startRange6
