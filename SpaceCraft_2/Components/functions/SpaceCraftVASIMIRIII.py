class PropulsionSystem:
    def __init__(self):
        self.primary_engine = "VASIMR Plasma Engine"
        self.secondary_engine = "Hybrid Methalox Engine"
        self.reaction_control = "Cold Gas Thrusters + Magnetic Nozzles"
        self.plasma_chamber = "Ion Cyclotron Resonance Field"
        self.energy_draw = "40 MW nominal (VASIMR), 2000 kN hybrid max thrust"

    def activate_plasma_drive(self, power_pct):
        print(f"VASIMR plasma engine active at {power_pct}% power")

    def ignite_hybrid_booster(self):
        print("Hybrid chemical booster ignition sequence started...")
