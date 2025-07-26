import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor("black")

# === 1. Cuerpo Central ===
def draw_main_body(x, y):
    ax.add_patch(patches.Rectangle((x, y), 2, 1, facecolor='gray', edgecolor='white'))
    ax.text(x + 0.3, y + 1.1, 'Cuerpo central', color='white')

# === 2. Brazos ===
def draw_arm(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color='silver', linewidth=4)

# === 3. Motor con hélice (propulsión) ===
def draw_motor(x, y):
    motor = patches.Circle((x, y), 0.2, facecolor='red', edgecolor='white')
    prop = patches.Circle((x, y), 0.4, facecolor='none', edgecolor='white', linestyle='--')
    ax.add_patch(motor)
    ax.add_patch(prop)
    ax.text(x - 0.3, y - 0.5, 'Motor', color='white')

# === 4. Láser montado al frente ===
def draw_laser(x, y):
    ax.add_patch(patches.Rectangle((x, y), 1, 0.3, facecolor='blue', edgecolor='white'))
    ax.plot([x + 1, x + 3], [y + 0.15, y + 0.15], color='red', linewidth=2)
    ax.text(x, y + 0.4, 'Láser', color='white')

# === 5. Estructura completa ===
# Cuerpo central
draw_main_body(4, 4)

# Brazos (tipo dron en X)
draw_arm(5, 4.5, 3, 6)
draw_motor(3, 6)

draw_arm(5, 4.5, 3, 3)
draw_motor(3, 3)

draw_arm(6, 4.5, 8, 6)
draw_motor(8, 6)

draw_arm(6, 4.5, 8, 3)
draw_motor(8, 3)

# Láser al frente (adelante del cuerpo)
draw_laser(6.5, 4.65)

# Ajustes visuales
ax.set_xlim(0, 12)
ax.set_ylim(2, 8)
ax.axis('off')
plt.title("Diseño 2D – Estructura + Propulsión + Láser", color='white')
plt.show()
