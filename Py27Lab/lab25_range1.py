import matplotlib.pyplot as plt
r1 = range(0, 20, 3)
print type(r1), len(r1), r1
plt.plot(r1, r1, 'r*')
plt.show()
