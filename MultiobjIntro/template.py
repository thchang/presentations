""" Tutorial for solving a toy inverse problem with ParMOO.

Before beginning:

pip install [--user] parmoo
pip install [--user] matplotlib

"""

import numpy as np

# Create a new data set of 3 pts in the plane
data = np.array([[-1, -1], [0, 1], [1, -1]])

from matplotlib import pyplot as plt

# Scatterplot to see what our dataset looks like
plt.scatter(data[:, 0], data[:, 1])
plt.show()

# Define some functions for our polynomial inverse problem:
#
# Find (a, b, c) s.t. f(x) = a x^2 + b x + c approximately satisfies:
#
#   f(data[0,0]) ~ data[0,1]
#   f(data[1,0]) ~ data[1,1]
#   f(data[2,0]) ~ data[2,1]
#
# AND
#
# a^2 + b^2 + c^2 is "small"

def poly(a, b, c, x):
    """ Evaluate the polynomial a x^2 + b x + c """

    return a * x ** 2 + b * x + c

def plot_poly(a, b, c):
    """ Plot the polynomial f(x) = a x^2 + b x + c """
    x_dat = np.linspace(-1, 1, 100)
    y_dat = np.array([poly(a, b, c, xi) for xi in x_dat])
    plt.plot(x_dat, y_dat)
    plt.scatter(data[:, 0], data[:, 1])

# Test our polynomial plotting function using matplotlib

plot_poly(1, 0, 0)
plt.show()

def my_sim(x):
    """ Define a vector-valued simulation that measures the error between the
    polynomial a x^2 + b x + c and the 3 points in ``data``.
    """

    return np.array([
                     poly(x["a"], x["b"], x["c"], data[0, 0]) - data[0, 1],
                     poly(x["a"], x["b"], x["c"], data[1, 0]) - data[1, 1],
                     poly(x["a"], x["b"], x["c"], data[2, 0]) - data[2, 1],
                    ])

# Begin solving the MOOP

# YOUR CODE HERE
