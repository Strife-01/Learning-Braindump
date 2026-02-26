import numpy as np

def equal(x: float, y: float, epsilon: float = 1e-9) -> bool:
    return np.abs(x - y) <= epsilon

def nthroot(x: float, n: int) -> float:
    if x == 0: return 0
    if x == 1: return 1
    
    y_o = x / n if x > 1 else 1.0

    while True:
        y_n = (1 / n) * ((n - 1) * y_o + x / (y_o ** (n - 1)))
        
        if equal(y_n, y_o):
            return y_n

        y_o = y_n
