import numpy as np

# Constantes simplificadas
G = 6.67430e-11  # Gravitational constant
c = 3e8          # Speed of light

def ergosphere_radius(mass, spin):
    """Radio de la ergosfera de un agujero negro de Kerr"""
    r_s = 2 * G * mass / c**2
    a = spin
    return r_s * (1 + np.cos(np.arccos(a)))

def extractable_energy(mass, spin):
    """Energía extraíble del agujero negro (máx 29% si spin=1)"""
    M = mass
    a = spin
    return M * c**2 * (1 - (1/np.sqrt(2)) * np.sqrt(1 + np.sqrt(1 - a**2)))

def ergosphere_boost(mass, spin, rest_mass):
    """Impulso generado por eyección de partículas en la ergosfera"""
    E = extractable_energy(mass, spin)
    return (E / rest_mass) * c

if __name__ == "__main__":
    mass_bh = 1e12  # kg, masa del agujero negro artificial
    spin = 0.95
    rest_mass_ship = 1e6  # kg

    r_erg = ergosphere_radius(mass_bh, spin)
    v_boost = ergosphere_boost(mass_bh, spin, rest_mass_ship)

    print(f"Radio de ergosfera: {r_erg:.2f} m")
    print(f"Velocidad máxima inducida por impulso: {v_boost/1000:.2f} km/s")
