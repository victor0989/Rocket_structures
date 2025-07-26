import matplotlib.pyplot as plt
import numpy as np

# Crear una figura
fig, ax = plt.subplots(figsize=(10, 6))

# Dibujar líneas del diseño (ejemplo: un diodo, resistencias, láser, etc.)
# Línea láser
ax.plot([1, 4], [5, 5], 'w', linewidth=2, label='Láser')

# Splitter
ax.plot([4, 5], [5, 6], 'w', linewidth=2, label='Beam Splitter')
ax.plot([4, 5], [5, 4], 'w', linewidth=2)

# Fotodetector
ax.plot([5, 6], [6, 6], 'w', linewidth=2, label='Fotodetector')

# Espejo
ax.plot([5, 6], [4, 4], 'w', linewidth=2, label='Espejo')

# Ajustes visuales
ax.set_facecolor("black")  # Fondo negro para líneas blancas
ax.set_xlim(0, 7)
ax.set_ylim(3, 7)
ax.set_aspect('equal')
ax.axis('off')
ax.legend()

# Guardar como imagen PNG
plt.savefig("laser_design.png", bbox_inches='tight', dpi=300)

