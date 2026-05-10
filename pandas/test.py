import matplotlib.pyplot as plt 
import numpy as np

decades = np.array([1980,1990,2000,2010, 2020])
home_prices = np.array([64600,122900,169000,221800,336900])
plt.figure()
plt.plot(decades, home_prices)
plt.show()