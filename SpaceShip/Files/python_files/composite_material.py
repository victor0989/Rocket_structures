# composite_material.py

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

class CompositeMaterial:
    def __init__(self, name, density, melting_point, thermal_conductivity,
                 tensile_strength, radiation_resistance,
                 thermal_expansion, plasma_resistance, gravitational_resistance):
        self.name = name
        self.density = density
        self.melting_point = melting_point
        self.thermal_conductivity = thermal_conductivity
        self.tensile_strength = tensile_strength
        self.radiation_resistance = radiation_resistance
        self.thermal_expansion = thermal_expansion
        self.plasma_resistance = plasma_resistance
        self.gravitational_resistance = gravitational_resistance

def visualize_material(material):
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('off')
    ax.text(0.5, 1.05, f"{material.name} - Composite Material", fontsize=16, ha='center', weight='bold')

    rect = Rectangle((0, 0), 1, 1, linewidth=2, edgecolor='black', facecolor='lightgray', alpha=0.1)
    ax.add_patch(rect)

    props = {
        "Density (kg/m³)": material.density,
        "Melting Point (K)": material.melting_point,
        "Thermal Conductivity (W/m·K)": material.thermal_conductivity,
        "Tensile Strength (MPa)": material.tensile_strength,
        "Radiation Resistance (0–1)": material.radiation_resistance,
        "Thermal Expansion (1/K)": material.thermal_expansion,
        "Plasma Resistance (0–1)": material.plasma_resistance,
        "Gravitational Resistance (G)": material.gravitational_resistance
    }

    y_pos = 0.9
    for prop, val in props.items():
        ax.text(0.05, y_pos, f"{prop}:", fontsize=10, weight='bold', va='center')
        ax.text(0.55, y_pos, f"{val}", fontsize=10, va='center')
        y_pos -= 0.1

    plt.tight_layout()
    plt.savefig("composite_material_profile.png", dpi=300)
    print("Image saved as composite_material_profile.png")

# Instancia del material y llamada
material = CompositeMaterial(
    name="UltraCarbon-X",
    density=1600,
    melting_point=4200,
    thermal_conductivity=150,
    tensile_strength=3500,
    radiation_resistance=0.95,
    thermal_expansion=1.1e-6,
    plasma_resistance=0.9,
    gravitational_resistance=150
)

visualize_material(material)


