
import math
from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

# Esta funcion sirve para realizar tanto el ajuste de y1 como de y2

def ajuste(y12,x1):
    tck = interpolate.splrep(x1, y12, s=0, k=3)
    x_new = np.linspace(min(x1), max(x1), 87600)
    y_fit = interpolate.BSpline(*tck)(x_new)
    return y_fit