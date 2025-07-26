# spacecraft_design.py

from dataclasses import dataclass, field
from typing import List, Dict


# 1. MATERIALS: FUSELAGE AND PROTECTION
@dataclass
class Material:
    name: str
    properties: List[str]


@dataclass
class Fuselage:
    type: str
    reinforcement: List[str]
    high_radiation_coating: List[str]
    shielding_materials: List[Material]


# 2. PROPULSION SYSTEM
@dataclass
class PropulsionComponent:
    name: str
    details: str


@dataclass
class PropulsionSystem:
    engine_type: str
    operation: str
    components: List[PropulsionComponent]
    materials: List[str]
    hybrid_options: List[str]


# 3. SENSORS AND ELECTRONIC SYSTEMS
@dataclass
class Sensor:
    type: str
    application: str


@dataclass
class ElectronicSystem:
    platform: str
    rtos: str
    data_bus: str
    sensors: List[Sensor]


# 4. THERMAL MANAGEMENT
@dataclass
class ThermalSystem:
    components: List[str]


# 5. STRUCTURAL DESIGN
@dataclass
class StructuralSection:
    section_name: str
    key_components: List[str]


# 6. SIMULATION TOOLS
@dataclass
class SimulationTools:
    control_modeling: List[str]
    physical_simulation: List[str]
    electronics_design: List[str]


# SPACESHIP WRAPPER CLASS
@dataclass
class SpacecraftDesign:
    fuselage: Fuselage
    propulsion: PropulsionSystem
    electronics: ElectronicSystem
    thermal: ThermalSystem
    structure: List[StructuralSection]
    simulation: SimulationTools


# INSTANTIATION EXAMPLE
def build_spacecraft_design() -> SpacecraftDesign:
    fuselage = Fuselage(
        type="Polymer matrix composites",
        reinforcement=["Carbon fiber (CFRP)", "Advanced ceramics"],
        high_radiation_coating=["Hybrid ceramic-matrix composites", "Titanium alloy", "Beryllium alloy"],
        shielding_materials=[
            Material("High-Density Polyethylene (HDPE)", ["Cosmic radiation shielding"]),
            Material("Boron compounds", ["Absorb alpha particles"]),
            Material("Lithium compounds", ["Neutron absorption"]),
            Material("Tantalum", ["Internal critical zone shielding"]),
            Material("Tungsten", ["High-density internal shielding"]),
        ]
    )

    propulsion = PropulsionSystem(
        engine_type="VASIMR",
        operation="Noble gas ionization via RF and magnetic acceleration",
        components=[
            PropulsionComponent("Superconducting solenoids", "Niobium-titanium at 20 K"),
            PropulsionComponent("RF injector", "13.56 MHz frequency"),
            PropulsionComponent("Expansion chamber", "For plasma acceleration")
        ],
        materials=["Niobium", "Zirconium", "Ceramic coatings"],
        hybrid_options=[
            "D–He3 plasma engine",
            "Liquid ammonia",
            "Metallic hydrogen (theoretical)"
        ]
    )

    electronics = ElectronicSystem(
        platform="Xilinx Zynq UltraScale+",
        rtos="FreeRTOS",
        data_bus="SpaceWire",
        sensors=[
            Sensor("LIDAR", "Collision avoidance"),
            Sensor("Thermal camera", "Thermal mapping"),
            Sensor("Spectral camera", "Spectral analysis"),
            Sensor("IMU", "Inertial navigation"),
            Sensor("Quantum gyroscope", "High-precision orientation")
        ]
    )

    thermal = ThermalSystem(
        components=[
            "Deployable radiators",
            "Sodium/lithium heat pipes",
            "Phase-change materials (PCM)"
        ]
    )

    structure = [
        StructuralSection("Nose", ["Ceramic coating", "Optical sensors", "LIDAR navigation"]),
        StructuralSection("Central cabin", ["Layered protection", "Control system", "FPGA actuators"]),
        StructuralSection("Rear engines", ["VASIMR", "Superconducting solenoids"]),
        StructuralSection("Wings", ["Integrated solar panels", "Lateral ion thrusters"]),
        StructuralSection("Outer hull", ["CFRP", "Polymer", "Radiation shield", "Thermal control layers"])
    ]

    simulation = SimulationTools(
        control_modeling=["MATLAB", "Simulink"],
        physical_simulation=["ANSYS", "COMSOL Multiphysics"],
        electronics_design=["KiCad", "Verilog", "VHDL"]
    )

    return SpacecraftDesign(
        fuselage=fuselage,
        propulsion=propulsion,
        electronics=electronics,
        thermal=thermal,
        structure=structure,
        simulation=simulation
    )


# Run and print basic summary
if __name__ == "__main__":
    spacecraft = build_spacecraft_design()
    print(spacecraft)
