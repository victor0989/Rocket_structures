import matplotlib.pyplot as plt

class ExoticObject:
    def __init__(self, name, mass, is_horizonless=True):
        self.name = name
        self.mass = mass
        self.is_horizonless = is_horizonless

    def is_viable_for_orbit(self, distance_km):
        rs = 2 * self.mass * 6.674e-11 / (3e8)**2  # Schwarzschild radius
        return distance_km * 1e3 > rs * 3

# Crear objetos estrella exótica
quark_star = ExoticObject("XTE J1739-285", 2e30)
dark_star = ExoticObject("Primordial Dark Star", 5e30, is_horizonless=True)

# Evaluar objetivos
objects = [quark_star, dark_star]
dist_km = 60000
results = []

for obj in objects:
    viable = obj.is_viable_for_orbit(dist_km)
    results.append((obj.name, viable))

# Visualización
labels = [name for name, _ in results]
statuses = ['Safe' if ok else 'Dangerous' for _, ok in results]
colors = ['green' if status == 'Safe' else 'red' for status in statuses]

fig, ax = plt.subplots()
bars = ax.bar(labels, [1]*len(labels), color=colors)
ax.set_ylim(0, 1.5)
ax.set_title("Orbital Safety of Exotic Objects")
ax.set_ylabel("Status")
ax.set_yticks([])

# Etiquetas de estado
for bar, status in zip(bars, statuses):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height + 0.05, status,
            ha='center', va='bottom', fontsize=12)

# Guardar como imagen PNG
image_path = "/mnt/c/Users/PC/PycharmProjects/pythonProject1/exotic_objects_orbital_safety.png"
plt.tight_layout()
plt.savefig(image_path)
image_path

