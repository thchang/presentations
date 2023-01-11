import numpy as np

# Create MOOP
from parmoo import MOOP
from parmoo.optimizers import LocalGPS
my_moop = MOOP(LocalGPS)

# Add a design variable
my_moop.addDesign({'name': "x1",
                   'des_type': "continuous",
                   'lb': 0.0, 'ub': 1.0})
# Add another just for demo
my_moop.addDesign({'name': "x2", 'des_type': "categorical",
                   'levels': 3})

# Define a simulation
def sim_func(x):
   if x["x2"] == 0:
      return np.array([(x["x1"] - 0.2) ** 2, (x["x1"] - 0.8) ** 2])
   else:
      return np.array([99.9, 99.9])

# Add the simulation with search and surrogate
from parmoo.searches import LatinHypercube
from parmoo.surrogates import GaussRBF
my_moop.addSimulation({'name': "MySim",
                       'm': 2,
                       'sim_func': sim_func,
                       'search': LatinHypercube,
                       'surrogate': GaussRBF,
                       'hyperparams': {'search_budget': 20}})

# Add the 2 objectives
my_moop.addObjective({'name': "f1", 'obj_func': lambda x, s: s["MySim"][0]})
my_moop.addObjective({'name': "f2", 'obj_func': lambda x, s: s["MySim"][1]})

# Add 3 acquisition functions
from parmoo.acquisitions import UniformWeights
my_moop.addAcquisition({'acquisition': UniformWeights,
                        'hyperparams': {}})
my_moop.addAcquisition({'acquisition': UniformWeights,
                        'hyperparams': {}})
my_moop.addAcquisition({'acquisition': UniformWeights,
                        'hyperparams': {}})

# Solve with 5 iterations
my_moop.solve(5)

# Get results
results = my_moop.getPF()

# Plot results
import matplotlib.pyplot as plt
plt.scatter(results['f1'], results['f2'])
plt.show()
