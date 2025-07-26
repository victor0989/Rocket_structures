import math
import random

class PropulsionSystem:
    def __init__(self, name, isp, thrust, propellant_type):
        self.name = name
        self.isp = isp  # Specific impulse (s)
        self.thrust = thrust  # Newtons
        self.propellant_type = propellant_type

    def compute_delta_v(self, initial_mass, final_mass):
        # Tsiolkovsky rocket equation
        g0 = 9.80665  # Earth gravity (m/s^2)
        delta_v = self.isp * g0 * math.log(initial_mass / final_mass)
        return delta_v

class Material:
    def __init__(self, name, density, radiation_resistance, thermal_emissivity):
        self.name = name
        self.density = density
        self.radiation_resistance = radiation_resistance
        self.thermal_emissivity = thermal_emissivity

    def is_suitable_for(self, environment_temp):
        return 100 <= environment_temp <= 300  # ideal operation range in K

class ThermalControl:
    def __init__(self, method, efficiency):
        self.method = method
        self.efficiency = efficiency

    def regulate(self, current_temp):
        if current_temp < 100:
            return "Heating required"
        elif current_temp > 300:
            return "Radiator active"
        return "Thermal balance maintained"

class PlasmaHarvester:
    def __init__(self, efficiency, collector_area):
        self.efficiency = efficiency
        self.collector_area = collector_area  # m^2

    def collect_energy(self, plasma_density):
        # Basic energy collection formula (simplified)
        return self.collector_area * plasma_density * self.efficiency

class AutonomousAI:
    def __init__(self, name="Optimus"):
        self.name = name
        self.energy_usage = 5.0  # kWh per cycle
        self.path_memory = []

    def decide_route(self, env_data):
        best_path = sorted(env_data, key=lambda e: e['threat'] + e['temp_variance'])[0]
        self.path_memory.append(best_path['id'])
        return best_path

# Example definitions
ion_engine = PropulsionSystem("Ion Drive (Xenon)", isp=3000, thrust=0.5, propellant_type="Xenon")
kevlar_composite = Material("Kevlar-Carbon Resin", density=1.44, radiation_resistance=8.5, thermal_emissivity=0.7)
radiator = ThermalControl(method="Passive Radiator", efficiency=0.85)
harvester = PlasmaHarvester(efficiency=0.25, collector_area=15.0)
autonomous_ai = AutonomousAI()

# Simulating Environment
environment_data = [
    {"id": "Node-A", "threat": 2, "temp_variance": 20},
    {"id": "Node-B", "threat": 4, "temp_variance": 10},
    {"id": "Node-C", "threat": 1, "temp_variance": 50},
]

if __name__ == "__main__":
    print("=== Δv Calculation ===")
    dv = ion_engine.compute_delta_v(initial_mass=1000, final_mass=750)
    print(f"{ion_engine.name} Δv: {dv:.2f} m/s\n")

    print("=== Material Evaluation ===")
    is_suitable = kevlar_composite.is_suitable_for(environment_temp=250)
    print(f"Kevlar is suitable for 250K environment? {is_suitable}\n")

    print("=== Thermal Control ===")
    status = radiator.regulate(current_temp=310)
    print(f"Thermal status: {status}\n")

    print("=== Plasma Harvesting ===")
    energy = harvester.collect_energy(plasma_density=0.005)
    print(f"Energy harvested: {energy:.3f} kW\n")

    print("=== Autonomous AI Route Planning ===")
    best_node = autonomous_ai.decide_route(environment_data)
    print(f"Selected path: {best_node['id']}, Path memory: {autonomous_ai.path_memory}")
