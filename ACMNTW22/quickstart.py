import numpy as np
from parmoo import MOOP, optimizers, searches, \
                   surrogates, acquisitions

# Create a MOOP object with LocalGPS solver
moop = MOOP(optimizers.LocalGPS)

# Add 2 design variables
moop.addDesign({"name": "x1", "des_type": "continuous",
                "lb": 0.0, "ub": 1.0})
moop.addDesign({"name": "x2", "des_type": "categorical",
                "levels": 3})

# Define and add 1 simulation with 2 outputs
def sim(x): return np.array([x["x1"]**2 + x["x2"],
                            (x["x1"] - 1)**2 + x["x2"]])
moop.addSimulation({"name": "MySim", "m": 2,
     "sim_func": sim, "search": searches.LatinHypercube,
     "surrogate": surrogates.GaussRBF})

# Add 2 objectives: minimize each sim output
def f1(x, s): return s["MySim"][0]
def f2(x, s): return s["MySim"][1]
moop.addObjective({"name": "f1", "obj_func": f1})
moop.addObjective({"name": "f2", "obj_func": f2})

# Add 1 constraint: x["x1"] <= 0.1
def g1(x, s): return 0.1 - x["x1"]
moop.addConstraint({"name": "g", "constraint": g1})

# Add 3 acquisition functions
for i in range(3):
   moop.addAcquisition({"acquisition":
            acquisitions.UniformWeights})

# Solve with 5 iterations and print the solution
moop.solve(5)
print(moop.getPF())
