from parmoo import MOOP
from parmoo.optimizers import LocalGPS as gps
from parmoo.searches import LatinHypercube as lhs
from parmoo.surrogates import GaussRBF as rbf
from parmoo.acquisitions import UniformWeights as wsum
# Create MOOP object with GPS optimizer
moop = MOOP(gps)
# Add a continuous + categorical design variable
moop.addDesign({'name': "x1", 'lb': 0.0, 'ub': 1.0})
moop.addDesign({'name': "x2", 'des_type': "cat", 'levels': 3})
# Define and add a simulation function (with surrogates and search)
def s(x): return [(x["x1"]-.2)**2, (x["x1"]-.8)**2] if x["x2"]==0 else [9,9]
moop.addSimulation({'name': "sim", 'm': 2, 'sim_func': s,
                    'search': lhs, 'surrogate': rbf})
# Add 2 objectives
moop.addObjective({'name': "f1", 'obj_func': lambda x, s: s["sim"][0]})
moop.addObjective({'name': "f2", 'obj_func': lambda x, s: s["sim"][1]})
# Add 3 weighted-sum acquisition functions
for i in range(3):
    moop.addAcquisition({'acquisition': wsum})
# Solve with 5 iterations and fetch numpy struct of solutions
moop.solve(5)
results = moop.getPF()
