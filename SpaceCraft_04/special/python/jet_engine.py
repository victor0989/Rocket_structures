class JetEngine:
    def __init__(self, diffuser, compressor, combustion_chamber, turbine, nozzle):
        self.diffuser = diffuser
        self.compressor = compressor
        self.combustion_chamber = combustion_chamber
        self.turbine = turbine
        self.nozzle = nozzle

    def describe(self):
        return {
            "Diffuser": "Slows airflow, increases pressure",
            "Compressor": "Raises pressure via turbine power",
            "Combustion": "Air-fuel combustion",
            "Turbine": "Thermal to mechanical energy",
            "Nozzle": "Accelerates exhaust gases"
        }
