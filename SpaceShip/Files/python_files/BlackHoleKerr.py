import math

class RotatingBlackHole:
    def __init__(self, mass, spin_parameter):
        """
        mass: en kg (masa del agujero negro)
        spin_parameter: a, adimensional, 0 <= a <= 1 (proporción de rotación)
        """
        self.mass = mass
        self.a = spin_parameter  # spin, entre 0 y 1

    def event_horizon_radius(self):
        """Radio del horizonte de eventos en metros (simplificado)"""
        G = 6.67430e-11  # Constante gravitacional
        c = 299792458    # Velocidad de la luz
        M = self.mass
        a = self.a * (G * M / c**2)  # Escala de spin convertida en metros
        r_plus = (G * M / c**2) * (1 + math.sqrt(1 - (a/(G*M/c**2))**2))
        return r_plus

    def ergosphere_radius(self, theta=math.pi/2):
        """Radio de la ergosfera en el plano ecuatorial (theta=pi/2)"""
        G = 6.67430e-11
        c = 299792458
        M = self.mass
        a = self.a * (G * M / c**2)
        r_ergo = (G * M / c**2) * (1 + math.sqrt(1 - (a/(G*M/c**2))**2 * math.cos(theta)**2))
        return r_ergo

# Ejemplo:
bh = RotatingBlackHole(mass=1e10 * 1.989e30, spin_parameter=0.9)  # Agujero negro supermasivo ~10^10 masas solares
print(f"Radio horizonte de eventos: {bh.event_horizon_radius():.2e} m")
print(f"Radio ergosfera (ecuatorial): {bh.ergosphere_radius():.2e} m")
