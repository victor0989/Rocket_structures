import sympy as sp

# Define coordinates: t, r, θ, φ
t, r, theta, phi = sp.symbols('t r theta phi')
M, a = sp.symbols('M a', real=True) # M = mass, a = specific spin (J/M)

# We define auxiliary functions
rho2 = r**2 + a**2 * sp.cos(theta)**2
Delta = r**2 - 2*M*r + a**2
Sigma = (r**2 + a**2)**2 - a**2 * Delta * sp.sin(theta)**2

# Kerr metric in Boyer–Lindquist coordinates
g = sp.MutableDenseNDimArray([[0]*4 for _ in range(4)], (4, 4))

# Non-null elements
g[0, 0] = -(1 - (2*M*r)/rho2)
g[0, 3] = -2*M*r*a*sp.sin(theta)**2 / rho2
g[3, 0] = g[0, 3]
g[1, 1] = rho2 / Delta
g[2, 2] = rho2
g[3, 3] = sp.sin(theta)**2 * (r**2 + a**2 + 2*M*r*a**2*sp.sin(theta)**2 / rho2)

# Symbolic simplification (optional)
g = sp.simplify(g)

# Show array
sp.pprint(g)