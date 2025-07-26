import math

# Given volume for all shapes
V = 1

# Sphere
# V = (4/3)*pi*r^3 -> r = (3V/(4pi))^(1/3)
r_sphere = (3 * V / (4 * math.pi)) ** (1/3)
A_sphere = 4 * math.pi * r_sphere**2

# Cube
# V = a^3 -> a = V^(1/3)
a_cube = V ** (1/3)
A_cube = 6 * a_cube**2

# Cylinder (height = diameter = 2r)
# V = pi*r^2*h, h=2r -> V = 2*pi*r^3 -> r = (V/(2*pi))^(1/3)
r_cyl = (V / (2 * math.pi)) ** (1/3)
h_cyl = 2 * r_cyl
A_cyl = 2 * math.pi * r_cyl**2 + 2 * math.pi * r_cyl * h_cyl

# Assuming solidification time t ~ (V / A)^2 (from your note on eq. 10.7)
t_sphere = (V / A_sphere) ** 2
t_cube = (V / A_cube) ** 2
t_cyl = (V / A_cyl) ** 2

print(f"Sphere: Surface Area = {A_sphere:.4f}, Solidification Time = {t_sphere:.4f}")
print(f"Cube: Surface Area = {A_cube:.4f}, Solidification Time = {t_cube:.4f}")
print(f"Cylinder: Surface Area = {A_cyl:.4f}, Solidification Time = {t_cyl:.4f}")

# Determine fastest and slowest solidification
times = {'Sphere': t_sphere, 'Cube': t_cube, 'Cylinder': t_cyl}
fastest = min(times, key=times.get)
slowest = max(times, key=times.get)

print(f"\nThe piece that solidifies first: {fastest}")
print(f"The piece that solidifies slowest: {slowest}")
