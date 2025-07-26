from dataclasses import dataclass, field
from typing import List, Optional

# --- Materiales ---

@dataclass
class Material:
    name: str
    properties: dict

# Ejemplos materiales
carbon_carbon = Material("Carbon-Carbon (C/C)", {"weight": "light", "heat_resistance": ">1370°C"})
titanium_6Al_4V = Material("Titanium 6Al-4V", {"strength": "high", "thermal_stability": "high"})
inconel_718 = Material("Inconel 718", {"heat_resistance": "extreme", "corrosion_resistance": "high"})
sapphire_glass = Material("Sapphire Glass", {"transparency": "UV", "impact_resistance": "high"})

# --- Herramientas de Soldadura ---

@dataclass
class WeldingTool:
    type: str  # 'laser' o 'arc'
    power_kw: float
    wavelength_nm: Optional[int] = None  # Solo para laser
    electrode_material: Optional[str] = None  # Solo para arc

# --- Manipuladores ---

@dataclass
class RoboticArm:
    length_m: float
    accuracy_mm: float
    protection: List[str]  # ej: ['thermal', 'plasma']

# --- Sistemas de Propulsion ---

@dataclass
class PropulsionSystem:
    type: str  # 'ion' o 'nuclear'
    thrust_N: float
    efficiency_percent: float
    fuel: Optional[str] = None  # 'xenon' o 'argon'

# --- Sensores ---

@dataclass
class Sensor:
    type: str  # 'LIDAR', 'thermal'
    precision_mm: Optional[float] = None
    range_m: Optional[float] = None

# --- Robot Completo ---

@dataclass
class SpaceRobot:
    name: str
    structure_material: Material
    coating_materials: List[Material]
    robotic_arms: List[RoboticArm]
    welding_tools: List[WeldingTool]
    propulsion_system: PropulsionSystem
    sensors: List[Sensor]
    weight_kg: float
    functions: List[str]

    def summary(self):
        print(f"Robot: {self.name}")
        print(f" Structure: {self.structure_material.name}")
        print(" Coating materials: " + ", ".join([m.name for m in self.coating_materials]))
        print(f" Weight: {self.weight_kg} kg")
        print(f" Functions: {', '.join(self.functions)}")
        print(f" Propulsion: {self.propulsion_system.type} - {self.propulsion_system.thrust_N} N thrust")
        print(f" Arms:")
        for i, arm in enumerate(self.robotic_arms, 1):
            print(f"  Arm {i}: Length {arm.length_m} m, Accuracy ±{arm.accuracy_mm} mm, Protection: {', '.join(arm.protection)}")
        print(" Welding Tools:")
        for tool in self.welding_tools:
            if tool.type == "laser":
                print(f"  Laser: {tool.power_kw} kW, {tool.wavelength_nm} nm")
            else:
                print(f"  Arc: {tool.power_kw} kW, Electrode: {tool.electrode_material}")
        print(" Sensors:")
        for sensor in self.sensors:
            print(f"  {sensor.type} Sensor - Precision: {sensor.precision_mm} mm, Range: {sensor.range_m} m")


# --- Instanciando un robot basado en tu descripción ---

robot = SpaceRobot(
    name="Autonomous Space Welding and Molding Robot",
    structure_material=carbon_carbon,
    coating_materials=[Material("Self-healing ceramics", {}), Material("Multilayer graphene shielding", {})],
    robotic_arms=[
        RoboticArm(length_m=3.0, accuracy_mm=0.1, protection=["thermal", "plasma"]),
        RoboticArm(length_m=2.5, accuracy_mm=0.1, protection=["thermal", "plasma"]),
    ],
    welding_tools=[
        WeldingTool(type="laser", power_kw=5, wavelength_nm=1064),
        WeldingTool(type="arc", power_kw=3, electrode_material="tungsten"),
    ],
    propulsion_system=PropulsionSystem(type="ion", thrust_N=50, efficiency_percent=40, fuel="xenon"),
    sensors=[
        Sensor(type="LIDAR", precision_mm=0.1, range_m=100),
        Sensor(type="thermal", precision_mm=None, range_m=50)
    ],
    weight_kg=400,
    functions=[
        "Laser welding in microgravity",
        "Material handling with plasma and metal powder",
        "Component molding with induction heat",
        "Additive manufacturing - metal 3D printing",
        "Autonomous self-repair"
    ]
)

robot.summary()
