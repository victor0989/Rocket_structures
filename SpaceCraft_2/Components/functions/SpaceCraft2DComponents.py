import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Crear figura y eje
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor("black")

# Función para dibujar un láser (como una caja con línea de salida)
def draw_laser(x, y):
    ax.add_patch(patches.Rectangle((x, y), 1, 0.5, edgecolor='white', facecolor='gray'))
    ax.plot([x + 1, x + 3], [y + 0.25, y + 0.25], color='red', linewidth=2)
    ax.text(x + 0.2, y + 0.6, 'Láser', color='white')

# Función para dibujar un beam splitter (cuadrado con dos salidas en diagonal)
def draw_beam_splitter(x, y):
    ax.add_patch(patches.Rectangle((x, y), 0.6, 0.6, edgecolor='white', facecolor='blue'))
    ax.plot([x + 0.3, x + 1.2], [y + 0.3, y + 1.2], color='white', linewidth=2)
    ax.plot([x + 0.3, x + 1.2], [y + 0.3, y - 0.6], color='white', linewidth=2)
    ax.text(x - 0.1, y + 0.7, 'Beam Splitter', color='white')

# Función para dibujar un espejo (línea vertical)
def draw_mirror(x, y):
    ax.plot([x, x], [y, y + 1], color='cyan', linewidth=3)
    ax.text(x - 0.3, y + 1.1, 'Espejo', color='white')

# Función para dibujar un fotodetector (rectángulo con entrada)
def draw_detector(x, y):
    ax.add_patch(patches.Rectangle((x, y), 1, 0.5, edgecolor='white', facecolor='green'))
    ax.text(x + 0.1, y + 0.6, 'Detector', color='white')

# Componentes en coordenadas específicas
draw_laser(1, 3)
draw_beam_splitter(4, 2.85)
draw_mirror(7, 2)
draw_detector(7, 4)

# Rayo láser que llega al splitter
ax.plot([2, 4], [3.25, 3.15], color='red', linewidth=2)

# Rayos saliendo del splitter
ax.plot([4.3, 7], [3.15, 2.5], color='yellow', linewidth=2)  # hacia el espejo
ax.plot([4.3, 7], [3.15, 4.25], color='yellow', linewidth=2)  # hacia el detector

# Ajustes de visualización
ax.set_xlim(0, 10)
ax.set_ylim(1, 6)
ax.axis('off')
plt.title("Diseño técnico 2D - Sistema Láser", color='white')
plt.show()
