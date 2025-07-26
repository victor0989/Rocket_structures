import matplotlib.pyplot as plt
import math

# (Tu código original aquí, sin cambios en las clases)
# --- INICIO DEL BLOQUE DE DISEÑO ---

class Spacecraft:
    def __init__(self, name):
        self.name = name
        self.mass = 50000  # kg
        self.fuselage = CompositeFuselage()
        self.engine = HybridPlasmaEngine()
        self.control_unit = FPGAControlSystem()
        self.shielding = RadiationShield()
        self.thermal = ThermalRegulation()
        self.orbit = OrbitDynamics()

    def status_report(self):
        return {
            "Mass (kg)": self.mass,
            "Thrust (N)": self.engine.calculate_thrust(),
            "Shield Efficiency": self.shielding.efficiency(),
            "Cooling Efficiency": self.thermal.efficiency(),
            "Navigation Stable": self.orbit.stable_orbit(),
        }

class CompositeFuselage:
    def __init__(self):
        self.material = "Carbon-Titanium Composite"
        self.layers = 3
        self.temperature_resistance = 3000  # K

class HybridPlasmaEngine:
    def __init__(self):
        self.type = "VASIMR + Hydrogen Alternative Fuel"
        self.ionization_chamber_temp = 100000  # Kelvin
        self.magnetic_field_strength = 5  # Tesla
        self.base_thrust = 15000  # Newtons

    def calculate_thrust(self):
        efficiency = 0.65
        return self.base_thrust * efficiency

class RadiationShield:
    def __init__(self):
        self.material = "Boron + Water + Graphene"
        self.radiation_flux = 0.85

    def efficiency(self):
        return f"{self.radiation_flux * 100}%"

class FPGAControlSystem:
    def __init__(self):
        self.logic_units = 4096
        self.sensor_latency = 1.2e-6

class ThermalRegulation:
    def __init__(self):
        self.cooling_fins = 12
        self.cooling_rate = 150

    def efficiency(self):
        return f"{self.cooling_rate} kW absorbed/sec"

class OrbitDynamics:
    def stable_orbit(self, gravity_source="magnetar", distance_km=100000):
        if gravity_source == "magnetar" and distance_km > 50000:
            return True
        return False

# --- FIN DEL BLOQUE DE DISEÑO ---

# Crear nave
ship = Spacecraft("Aetherion MkII")
report = ship.status_report()

# Convertir el status report a texto visualizable
lines = [f"{key}: {value}" for key, value in report.items()]
full_text = "\n".join(lines)

# Crear imagen
fig, ax = plt.subplots(figsize=(6, 4))
ax.axis('off')
ax.text(0.01, 0.95, f"Spacecraft Report: {ship.name}\n\n{full_text}", fontsize=12, va='top', family='monospace')

# Guardar como PNG
plt.savefig("spacecraft_status.png", bbox_inches='tight', dpi=300)
plt.show()
