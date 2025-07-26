import numpy as np
import matplotlib.pyplot as plt

# Parámetros del agujero negro
M = 1  # masa arbitraria
a = 0.8  # espín (0 <= a < M)

# Coordenadas ergosfera y horizonte de eventos
r_plus = M + np.sqrt(M**2 - a**2)
r_erg = lambda theta: M + np.sqrt(M**2 - a**2 * np.cos(theta)**2)

# Malla polar
theta = np.linspace(0, 2*np.pi, 400)
r1 = np.array([r_erg(t) for t in theta])
r2 = np.full_like(theta, r_plus)

# Conversión a coordenadas cartesianas
x1, y1 = r1 * np.cos(theta), r1 * np.sin(theta)
x2, y2 = r2 * np.cos(theta), r2 * np.sin(theta)

# Visualización
plt.figure(figsize=(6, 6))
plt.fill(x1, y1, 'orange', alpha=0.5, label='Ergosfera')
plt.fill(x2, y2, 'black', alpha=0.7, label='Horizonte de eventos')

# Trayectorias ficticias relativistas
for angle in np.linspace(0, 2*np.pi, 8):
    r = np.linspace(r_plus, 10, 300)
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    plt.plot(x, y, 'cyan', lw=0.8)

plt.title("Estructura del agujero negro de Kerr (ergosfera y horizonte)")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.show()
