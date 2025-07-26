import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_facecolor("black")

# === Modules Drawing ===
def draw_module(x, y, width, height, label, color="deepskyblue"):
    ax.add_patch(patches.Rectangle((x, y), width, height, facecolor=color, edgecolor='white', linewidth=1.5))
    ax.text(x + width/2, y + height + 0.2, label, color='white', ha='center', fontsize=8)

# === Connectors ===
def draw_line(x1, y1, x2, y2):
    ax.plot([x1, x2], [y1, y2], color='white', linewidth=1, linestyle='--')

# === Main Modules ===
draw_module(5, 8.5, 2, 0.8, "Plasma Injector\n(VASIMR Nozzle)", "orange")
draw_module(5, 7.4, 2, 0.8, "Ionization Chamber", "orangered")
draw_module(5, 6.3, 2, 0.8, "Magnetic Containment\nCoils", "purple")
draw_module(5, 5.2, 2, 0.8, "Gravity Manipulation\nCore", "slateblue")
draw_module(5, 4.1, 2, 0.8, "Micro Black Hole\nReactor", "darkred")
draw_module(5, 3.0, 2, 0.8, "Power Distribution\nArray", "green")
draw_module(5, 1.9, 2, 0.8, "Thermal Radiation\nShields", "lightgrey")
draw_module(2, 7.4, 2, 0.8, "Navigation Control\nUnit", "dodgerblue")
draw_module(8, 7.4, 2, 0.8, "Fusion Pre-Stabilizer", "cyan")
draw_module(5, 0.8, 2, 0.8, "Quantum Field\nStabilizer", "gold")

# === Additional Sensors & Systems ===
draw_module(2, 9, 1.5, 0.6, " LIDAR Sensor", "lime")
draw_module(8.5, 9, 1.5, 0.6, " Antenna Array", "lime")
draw_module(2, 2.2, 1.5, 0.6, " Battery Core", "yellow")
draw_module(8.5, 2.2, 1.5, 0.6, " FPGA/RTOS", "magenta")

# === Connect Systems ===
draw_line(6, 9.3, 6, 9)
draw_line(6, 8.5, 6, 8.2)
draw_line(6, 7.4, 6, 7.1)
draw_line(6, 6.3, 6, 6)
draw_line(6, 5.2, 6, 4.9)
draw_line(6, 4.1, 6, 3.8)
draw_line(6, 3.0, 6, 2.7)
draw_line(6, 1.9, 6, 1.6)
draw_line(6, 0.8, 6, 0.5)

draw_line(3.5, 9.0, 5, 8.9)
draw_line(9.2, 9.0, 7, 8.9)
draw_line(3.5, 2.5, 5, 2.3)
draw_line(9.2, 2.5, 7, 2.3)

# Final Adjustments
ax.set_xlim(0, 12)
ax.set_ylim(0, 10.5)
ax.axis('off')
plt.title(" Futuristic Spacecraft Control System (Python 2D Schematic)", color='white', fontsize=14)
plt.show()
