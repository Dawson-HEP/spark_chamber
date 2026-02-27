import numpy as np
from itertools import combinations

POS = np.array([[0, 1, 0], [1, 0, 0], [1, 1, 0], [0.5, 0.5, np.sqrt(2) / 2]])
TIME = np.array([0.0020616 - 0.8, 0.0020615 - 0.8, 0.0020615 - 0.8, 0.0020615 - 0.8])
VEL = 343


comb = list(combinations(range(len(POS)), 2))
augmented_matrix = np.empty((len(comb), 5), dtype=np.float32)
coeff, const = augmented_matrix[:, 0:4], augmented_matrix[:, -1]

for n, (i, j) in enumerate(comb):
    vec_i, vec_j = POS[i], POS[j]
    t_i, t_j = TIME[i], TIME[j]

    const[n] = (
        np.dot(vec_i, vec_i)
        - (t_i**2) * (VEL**2)
        - np.dot(vec_j, vec_j)
        + (t_j**2) * (VEL**2)
    )
    coeff[n, 0:3] = -2 * (vec_j - vec_i)
    coeff[n, 3] = 2 * (t_j - t_j)

x, residuals, rank, s = np.linalg.lstsq(coeff, const, rcond=None)

print(f"position {x}")
...
