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

from parmoo import MOOP
from parmoo.optimizers import LocalGPS

# Create a MOOP object that solves optimization problems using LocalGPS (DFO)
my_moop = MOOP(LocalGPS)

# Add 3 design variables, "a", "b", and "c"
my_moop.addDesign({"name": "a", "lb": -10.0, "ub": 10.0})
my_moop.addDesign({"name": "b", "lb": -10.0, "ub": 10.0})
my_moop.addDesign({"name": "c", "lb": -10.0, "ub": 10.0})

from parmoo.searches import LatinHypercube
from parmoo.surrogates import GaussRBF

# Add the simulation function, with a LH DOE (50 evals) and Gaussian RBF surrogate
my_moop.addSimulation({"name": "My Simulation Function",
                       "m": 3,
                       "sim_func": my_sim,
                       "search": LatinHypercube,
                       "surrogate": GaussRBF,
                       "hyperparams": {"search_budget": 50}})

# Add the Chi squared of sim errors as an objective to minimize
my_moop.addObjective({"name": "Chi squared error",
                      "obj_func": lambda x, s: np.linalg.norm(s["My Simulation Function"]) ** 2})
# Add an L2 regularization penalty
my_moop.addObjective({"name": "L2 Regularization",
                      "obj_func": lambda x, s: x["a"] ** 2 + x["b"] ** 2 + x["c"] ** 2})

from parmoo.acquisitions import UniformWeights

# Add 5 acquisition functions (batch sizes of 5), which generate uniform random weights
for i in range(5):
    my_moop.addAcquisition({"acquisition": UniformWeights})

# Solve with 10 iterations (10 * 5 + 50 = 100 sim evals)
my_moop.solve(10)

# Extract the final Pareto front
my_pf = my_moop.getPF()

# Plot the Chi squared error vs L2 penalty
plt.scatter(my_pf["Chi squared error"], my_pf["L2 Regularization"])
plt.xlabel("Chi squared error")
plt.ylabel("L2 Regularization")
plt.show()

# Plot the resulting polynomials
for pt in my_pf:
    plot_poly(pt["a"], pt["b"], pt["c"])
plt.show()
