import matplotlib.pyplot as plt
import numpy as np

arr1 = np.random.random(size=(3, 3))
arr2 = np.arange(0, 9).reshape(3, 3)
plt.figure()
plt.plot(arr1)
plt.plot(arr2)
plt.show()