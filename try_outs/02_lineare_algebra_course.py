import numpy as np
from icecream import ic

v = np.array([1, 2, 3])  # -> vektorisierte liste, kein lin alg object

# for tensors just make more lists
tensor = np.array([[[[1], [2]], [[3], [4]], [[5], [6]]]])
ic(tensor)

# Broadcasting
# numpy does smart stuff in the background (erweiterung)
# it does it only if the dimensions work and is clear

# mathematically incorrect np.array([[1], [2]]) + 1
# is done even if it is mathematically not correct because rules are simple
o = np.array([[1], [2]]) + 1
# numpy makes a vector in the background
ic(o)
