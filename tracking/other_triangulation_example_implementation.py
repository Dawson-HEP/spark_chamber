import numpy as np
from dataclasses import dataclass

SPEED_OF_SOUND = 343.0

@dataclass
class Point:
    x: float
    y: float
    z: float
    dt: float

    def sum_p_squared(self):
        return self.x**2 + self.y**2 + self.z**2

    def t_squared(self):
        return self.dt**2


def triangulate(p1, p2, p3, p4):
    v = SPEED_OF_SOUND

    p_list = [Point(*p1), Point(*p2), Point(*p3), Point(*p4)]

    pairs = [
        [p_list[0], p_list[1]],
        [p_list[0], p_list[2]],
        [p_list[0], p_list[3]],
        [p_list[1], p_list[2]],
    ]

    A_rows = []
    b_rows = []

    for pA, pB in pairs:
        A_rows.append([
            2.0 * (pA.x - pB.x),
            2.0 * (pA.y - pB.y),
            2.0 * (pA.z - pB.z),
            2.0 * v * v * (pA.dt - pB.dt),
        ])

        b_rows.append(
            pA.sum_p_squared()
            - pB.sum_p_squared()
            - v * v * (pA.t_squared() - pB.t_squared())
        )

    A = np.array(A_rows, dtype=float)
    b = np.array(b_rows, dtype=float)

    solution, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

    return A, solution


def main():
    p1 = (0.0, 0.0, 0.0, 0.002357)
    p2 = (1.0, 0.0, 0.0, 0.002357)
    p3 = (0.0, 1.0, 0.0, 0.002357)
    p4 = (1.0, 1.0, 0.0, 0.002357)

    A, solution = triangulate(p1, p2, p3, p4)

    print(A)
    print(f"<x, y, z, dt> = {solution}")


if __name__ == "__main__":
    main()

