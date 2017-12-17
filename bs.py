import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.arange(-5, 5, 0.5)
y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(x, y)
F = 3 + 2*X + 4*X*Y + 5*X*X

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, F)
plt.show()