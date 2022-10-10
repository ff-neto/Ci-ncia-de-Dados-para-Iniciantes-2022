import numpy as np
import sys

a = [1, 2, 3, 4, 5]
b = np.array([1, 2, 3, 4, 5])


print(a)
print(b)


# -----------------------------------------------------
# a lista gasta mas memória do que um array
sys.getsizeof(a)
# 112


# -----------------------------------------------------
# a lista numpy gasta menos memória
b.nbytes
#40
