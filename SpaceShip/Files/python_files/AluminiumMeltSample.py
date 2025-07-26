# Diseño básico en Python de un sistema de fundición para metales tipo carbono-carbón en el espacio,
# considerando variables de temperatura, solubilidad, defectos y simulación de enfriamiento.

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

# Modelo de enfriamiento y generación de defectos
def porosity_defect_estimator(solubility_liquid, solubility_solid):
    """Porosidad potencial por exceso de gas al solidificar"""
    delta_sol = solubility_liquid - solubility_solid
    if delta_sol > 0.5:
        return "High microporosity risk (Swiss cheese appearance)"
    elif delta_sol > 0.2:
        return "Moderate porosity, control degassing recommended"
    else:
        return "Low risk of porosity"

# Visualización de la curva de solubilidad
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
plt.show()

# Diagnóstico
diagnosis = porosity_defect_estimator(al_413.hydrogen_solubility_liquid, al_413.hydrogen_solubility_solid)
print("Defect Risk Diagnosis:", diagnosis)

# Componentes del sistema de fundición
class CastingSystem:
    def __init__(self, mold_material, use_internal_chillers=True):
        self.mold_material = mold_material
        self.use_internal_chillers = use_internal_chillers

    def describe(self):
        print(f"Mold material: {self.mold_material}")
        print("Chillers: ", "Internal and External" if self.use_internal_chillers else "External only")
        print("Design focus: Avoid shrinkage porosity and promote uniform solidification.")

# Crear un sistema de fundición ejemplo
foundry = CastingSystem("H13 Tool Steel", use_internal_chillers=True)
foundry.describe()
