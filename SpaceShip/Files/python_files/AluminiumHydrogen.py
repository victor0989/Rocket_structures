import numpy as np
import matplotlib.pyplot as plt

# Propiedades de materiales típicos en fundición espacial
class Metal:
    def __init__(self, name, melting_point, hydrogen_solubility_liquid, hydrogen_solubility_solid):
        self.name = name
        self.melting_point = melting_point  # °C
        self.hydrogen_solubility_liquid = hydrogen_solubility_liquid  # ppm
        self.hydrogen_solubility_solid = hydrogen_solubility_solid  # ppm

    def solubility_curve(self, temperature):
        """Modelo simplificado de solubilidad del hidrógeno según la fase"""
        if temperature > self.melting_point:
            return self.hydrogen_solubility_liquid
        else:
            return self.hydrogen_solubility_solid

# Ejemplo: Aleación de aluminio 413.0
al_413 = Metal("Aluminum Alloy 413.0", melting_point=570, hydrogen_solubility_liquid=0.69, hydrogen_solubility_solid=0.04)

# Simulación del proceso de enfriamiento y cambio de solubilidad
def simulate_solidification(metal, start_temp, end_temp, steps=100):
    temps = np.linspace(start_temp, end_temp, steps)
    solubilities = [metal.solubility_curve(t) for t in temps]
    return temps, solubilities

# Visualización de la curva de solubilidad y guardado como PNG
temps, sol = simulate_solidification(al_413, 700, 500)

plt.figure(figsize=(8, 4))
plt.plot(temps, sol, label=f"{al_413.name}")
plt.axvline(al_413.melting_point, color='red', linestyle='--', label="Melting Point")
plt.title("Hydrogen Solubility vs Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Hydrogen Solubility (ppm)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Guardar la figura como PNG
output_path = "/mnt/c/Users/PC/PycharmProjects/pythonProject1hydrogen_solubility_aluminum.png"
plt.savefig(output_path)
plt.close()

output_path
