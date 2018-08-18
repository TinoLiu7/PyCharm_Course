import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

mu = 80
sigma = 8
x = mu + sigma * np.random.randn(10000)
print len(x)
num_bins = 50
n, bins, patches = plt.hist(x, num_bins, density=1, facecolor='blue', alpha=0.5)
y = mlab.normpdf(bins, mu, sigma)
plt.plot(bins, y, 'r*-')
plt.show()