import numpy as np
import matplotlib.pyplot as plt

# Initial parameters
N = 1000 # Number of points
theta = np.linspace(0, 2 * np.pi, N) # Angle in polar coordinates

# Function to generate Penrose structures
def penrose_structure(theta, scale=1):
r = scale * (1 + 0.3 * np.sin(5 * theta)) # Fractal radial variation
x = r * np.cos(theta)
y = r * np.sin(theta)
return x, y

# Simulation of the magnetar's electromagnetic field
def magnetar_field(x, y):
field_strength = np.sqrt(x**2 + y**2) * np.exp(-0.01 * (x**2 + y**2))
return field_strength

# Generating the Penrose structure and field
x, y = penrose_structure(theta, scale=5)
field = magnetar_field(x, y)

# Visualization
plt.figure(figsize=(8, 8))
plt.scatter(x, y, c=field, cmap='inferno', s=5)
plt.colorbar(label="Electromagnetic field strength")
plt.title("Simulation of Penrose structures in a magnetar field")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.show()