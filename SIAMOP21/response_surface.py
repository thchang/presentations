import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
import numpy as np
from pyDOE import lhs

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
Z = 1.5*X + (X**2 + Y**2) * 0.25 + 0.1 * X**3

pts = lhs(2, 20) * 10.0 - 5.0
xpts = pts[:, 0]
ypts = pts[:, 1]
zpts = 1.5*xpts + (xpts**2 + ypts**2) * 0.25 + 0.1 * xpts**3

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, linewidth=0, antialiased=False, alpha=0.5)
ax.scatter(xpts, ypts, zpts, color='r', s=40, alpha=1)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

plt.show()

