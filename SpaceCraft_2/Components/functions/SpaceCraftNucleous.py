class SpacecraftCore:
    def __init__(self):
        self.name = "Falcon-X Plasma Hybrid"
        self.fuselage_material = "Carbon-Titanium Composite"
        self.structural_design = "Reinforced with active shock absorption"
        self.optimized_for = ["Weak atmospheres", "High radiation zones", "Low gravity docking"]

    def describe(self):
        print(f"Spacecraft: {self.name}")
        print(f"Fuselage: {self.fuselage_material}")
        print("Optimized for:", ", ".join(self.optimized_for))
