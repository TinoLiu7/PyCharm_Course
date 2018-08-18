import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

randomSequences = pd.DataFrame(np.random.normal(1.0, 0.07, (100, 8)))
print randomSequences.head()
# 3rd 1*2*3
accumulates = randomSequences.cumprod()
print accumulates.head()
accumulates.plot()
plt.show()
