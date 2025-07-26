# -------------------------------------------------------------
# Exercise 23.4 – Einstein Curvature Tensor in Schwarzschild Coordinates
# -------------------------------------------------------------
# Calculate G_{μν} = R_{μν} - (1/2) R g_{μν}
# Then transform to orthonormal frame using tetrads (vierbein)

from sympy import symbols, simplify, Function, Matrix
from sympy.tensor.tensor import TensorIndexType, tensor_indices, TensorHead

# Define coordinates and metric components
t, r, theta, phi = symbols('t r theta phi')
M = symbols('M')  # mass
g_tt = -(1 - 2*M/r)
g_rr = 1 / (1 - 2*M/r)
g_thth = r**2
g_phph = r**2 * (sin(theta))**2

# Placeholder metric tensor in Schwarzschild coordinates
g = Matrix([
    [g_tt, 0,     0,           0],
    [0,    g_rr,  0,           0],
    [0,    0,     g_thth,      0],
    [0,    0,     0,           g_phph]
])

# Define placeholder Ricci tensor and scalar curvature (symbolic form)
R = symbols('R')  # scalar curvature
Rmn = Matrix(symbols('R00 R11 R22 R33')).reshape(4, 1)

# Compute Einstein tensor (symbolic)
Gmn = Rmn - (1/2)*R*g

# Transformation to orthonormal frame (see eqs. 23.15a,b)
# G_hat_ab = e^μ_a e^ν_b G_{μν}
# Requires defining tetrads e^μ_a (not expanded here)

# -------------------------------------------------------------
# Exercise 23.5 – Total Number of Baryons in a Star
# -------------------------------------------------------------
# A = ∫ 4π r² n(r) e^{A(r)} dr  from r = 0 to R

from sympy import Integral, exp, pi

r, R = symbols('r R')
n = Function('n')(r)
A_func = Function('A')(r)

A_total = Integral(4 * pi * r**2 * n * exp(A_func), (r, 0, R))

# -------------------------------------------------------------
# Exercise 23.6 – Buoyant Force in a Star
# -------------------------------------------------------------
# F_buoy = -dp/dr * V,     F_grav = (ρ + p) * m/r² * V

from sympy import Derivative

p, rho, m, V = symbols('p rho m V', positive=True)
F_buoy = -Derivative(p, r) * V
F_grav = (rho + p) * m / r**2 * V

# Newtonian: F_grav = rho * m / r² * V

# -------------------------------------------------------------
# Exercise 23.7 – Gravitational Energy of a Newtonian Star
# -------------------------------------------------------------
# Use:
# ∇²ϕ = 4πρ  (Laplace),      Hydrostatic eq: dP/dr = -ρ dϕ/dr
# Total gravitational energy U ~ -∫ (G m(r) ρ / r) 4πr² dr

phi = Function('phi')(r)
rho = Function('rho')(r)
m = Function('m')(r)

grav_energy_1 = Integral(rho * phi * 4*pi*r**2, (r, 0, R))
grav_energy_2 = Integral(rho * m / r * 4*pi*r**2, (r, 0, R))

# Equivalent forms:
# U = -1/2 ∫ ϕ 4πr²ρ dr
# U = - ∫ (ϕ²) 4πr²ρ dr
# U = -3 ∫ 4πr²ρ dr (constant density approx)

# -------------------------------------------------------------
# Schwarzschild Exterior Metric (for reference)
# -------------------------------------------------------------
# ds² = -(1 - 2M/r) dt² + (1 - 2M/r)⁻¹ dr² + r² dΩ²

g_ext = Matrix([
    [-(1 - 2*M/r), 0,         0,           0],
    [0,            1/(1 - 2*M/r), 0,       0],
    [0,            0,         r**2,        0],
    [0,            0,         0,       r**2 * sin(theta)**2]
])
