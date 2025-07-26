from dataclasses import dataclass, field
from typing import List, Dict, Optional

# Definimos un material
@dataclass
class Material:
    name: str
    properties: Dict[str, str]  # e.g. {'thermal_reflectance': '99%', 'max_temp_C': '1370'}
    description: Optional[str] = None

# Componente del robot o de la nave
@dataclass
class Component:
    name: str
    material: Material
    function: str
    properties: Dict[str, str] = field(default_factory=dict)  # ej. precisión, rango

# Sistema integrado del robot
@dataclass
class IntegratedSystem:
    name: str
    description: str
    components: List[Component] = field(default_factory=list)

    def add_component(self, component: Component):
        self.components.append(component)

# Secuencia de misión como pasos
@dataclass
class MissionStep:
    step_number: int
    description: str

@dataclass
class MissionSequence:
    steps: List[MissionStep]

    def run_sequence(self):
        for step in self.steps:
            print(f"Step {step.step_number}: {step.description}")
            # Aquí podrías simular cada acción o evento

# --- Crear materiales ---
carbon_carbon = Material(
    name="Carbon-Carbon (C/C)",
    properties={"weight": "lightweight", "structure": "multi-layered reinforced"},
    description="Structural frame for chassis and superstructure"
)

white_alumina = Material(
    name="White Alumina (Al2O3)",
    properties={"thermal_reflectance": "99%", "resistance": "UV spectrum"},
    description="Anti-radiation ceramic coating"
)

titanium_alloy = Material(
    name="Titanium 6Al-4V",
    properties={"strength": "high", "thermal_stability": "good"},
    description="Arm structure material"
)

inconel_718 = Material(
    name="Inconel 718",
    properties={"heat_resistance": "maintains mechanical properties in heat"},
    description="Joints and actuators"
)

# --- Crear componentes ---
chassis = Component(
    name="Chassis / Superstructure",
    material=carbon_carbon,
    function="Lightweight, reinforced structural frame"
)

heat_shield = Component(
    name="Heat Shield and Front",
    material=Material(
        name="Carbon-carbon + Composite with carbon foam",
        properties={"max_temp_C": "1370"},
        description="Protects against extreme temperatures"
    ),
    function="Thermal protection"
)

arm_structure = Component(
    name="Robotic Arm Structure",
    material=titanium_alloy,
    function="Lightweight, strong, thermally stable"
)

joint_actuators = Component(
    name="Joints and Actuators",
    material=inconel_718,
    function="Maintain mechanical properties under heat"
)

# --- Sistemas integrados ---
propulsion_system = IntegratedSystem(
    name="Internal Propulsion",
    description="Ion engines with xenon or argon propellant"
)

propulsion_system.add_component(Component(
    name="Ion Engine",
    material=Material(name="Various metals", properties={}, description="Ion thruster"),
    function="Thrust generation 1-100 N"
))

welding_system = IntegratedSystem(
    name="Welding System",
    description="Vacuum TIG or Nd:YAG laser welding"
)

# --- Secuencia de misión ---
mission_steps = [
    MissionStep(1, "Spacecraft approaches a region of stable orbit"),
    MissionStep(2, "Robotic arms deploy instruments and begin plasma sampling"),
    MissionStep(3, "Collected matter is analyzed or stored"),
    MissionStep(4, "Onboard printers and welders manufacture parts as needed"),
    MissionStep(5, "Data transmitted using quantum-secure channels"),
    MissionStep(6, "Spacecraft may reposition or return after cycle completes"),
]

mission = MissionSequence(mission_steps)

# Ejecutar secuencia (simulación simple)
if __name__ == "__main__":
    mission.run_sequence()
