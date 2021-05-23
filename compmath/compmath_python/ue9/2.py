import numpy as np


def maximum(v):
    return np.max(v)


def cap(v):
    v[abs(v) > maximum(v)] = - maximum(v)
    return v


if __name__ == "__main__":
    v = np.array([1, 5, 42, -100, -6])
    print(maximum(v))
    print(cap(v))
