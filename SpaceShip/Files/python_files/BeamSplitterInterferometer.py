from qutip import *
import numpy as np
import matplotlib.pyplot as plt

# Estados de entrada en un beam splitter (coherente y vacío)
alpha = 1.0
psi1 = coherent(10, alpha)
psi2 = vacuum(10)
psi_in = tensor(psi1, psi2)

# Operador beam splitter
theta = np.pi / 4  # 50/50
BS = tensor(qeye(10), qeye(10))
BS = (tensor(destroy(10), qeye(10)) + tensor(qeye(10), destroy(10))).unit()

# Estado de salida
psi_out = BS * psi_in
