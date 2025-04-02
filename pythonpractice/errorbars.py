import matplotlib.pyplot as plt
import numpy as np
import random

x = np.zeros(20)
y = np.zeros_like(x)
y_err = np.zeros_like(x)

for i in range(x.shape[0]):
    x[i] = random.randint(0, 15)
    y[i] = random.randint(0, 15)
    y_err[i] = random.randint(0,5)

plt.plot(x,y, 'b,')
plt.errorbar(x, y, yerr=y_err, fmt='o', capsize=5)
plt.grid()
plt.show()