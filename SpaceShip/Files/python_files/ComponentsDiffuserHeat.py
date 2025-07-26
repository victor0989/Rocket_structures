import math

# ----------------------------
# THERMAL CONTROL SYSTEM
# ----------------------------

class ThermalControlSystem:
    def __init__(self):
        self.oper_temp_range = (20, 150)  # °C
        self.survival_temp_range = {
            "wet": (10, 190),
            "dry": (-80, -130)
        }
        self.heat_dissipation_w = {9.86: 6400}  # Rs: watts

    def heat_dissipation(self, distance_rs):
        return self.heat_dissipation_w.get(distance_rs, None)

# ----------------------------
# SHIELDING MATERIALS
# ----------------------------

class ShieldingMaterial:
    def __init__(self, name, composition, purpose):
        self.name = name
        self.composition = composition
        self.purpose = purpose

    def describe(self):
        return f"{self.name}: {self.composition}, used for {self.purpose}"

# ----------------------------
# BLACK HOLE METRICS
# ----------------------------

class BlackHoleMetric:
    def __init__(self, type_name, description):
        self.type_name = type_name
        self.description = description

    def summary(self):
        return f"{self.type_name} describes: {self.description}"

# ----------------------------
# COMPRESSOR CALCULATIONS
# ----------------------------

class CompressorCalculations:
    def __init__(self, cp=1005):
        self.cp = cp  # J/kg·K

    def slip_factor(self, C_theta2, U2):
        return 1 - (C_theta2 / U2)

    def delta_T0(self, U2, C_theta2, U1, C_theta1):
        return (U2 * C_theta2 - U1 * C_theta1) / self.cp

    def mass_flow_rate(self, P01, T01, A, C1, R=287):
        rho = P01 / (R * T01)
        return rho * A * C1

    def inlet_velocity(self, delta_T01):
        return math.sqrt(2 * self.cp * delta_T01)

    def rotational_speed(self, U1, D1):
        return U1 / (math.pi * D1)

    def compressor_power(self, mdot, delta_T0):
        return mdot * self.cp * delta_T0

# ----------------------------
# JET ENGINE COMPONENT
# ----------------------------

class JetEngineComponent:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def info(self):
        return f"{self.name}: {self.function}"

# ----------------------------
# SPACECRAFT SYSTEM
# ----------------------------

class SpacecraftSystem:
    def __init__(self, component, role):
        self.component = component
        self.role = role

# ----------------------------
# SAMPLE DATA
# ----------------------------

# Black hole metrics
metrics = [
    BlackHoleMetric("Frolov", "Spacetime near black holes with charge and rotation"),
    BlackHoleMetric("Schwarzschild", "Spherical, non-rotating black holes"),
    BlackHoleMetric("Kerr", "Rotating black holes")
]

# Jet Engine Components
jet_components = [
    JetEngineComponent("Diffuser", "Slows down airflow and increases pressure."),
    JetEngineComponent("Compressor", "Increases air pressure via turbine energy."),
    JetEngineComponent("Combustion Chamber", "Air-fuel combustion location."),
    JetEngineComponent("Turbine", "Converts thermal to mechanical energy."),
    JetEngineComponent("Nozzle", "Accelerates gases for thrust.")
]

# Shielding
shield = ShieldingMaterial(
    "Primary Shield", "Carbon–Carbon composite (C–C)", "Radiation and thermal shielding near the Sun."
)

# Example usage:
if __name__ == "__main__":
    tcs = ThermalControlSystem()
    print("Heat dissipation at 9.86 Rs:", tcs.heat_dissipation(9.86), "W")
    print(shield.describe())

    for m in metrics:
        print(m.summary())

    for j in jet_components:
        print(j.info())
