def penrose_extraction_efficiency(spin):
    """
    Estimación simple de eficiencia energética basada en el spin del agujero negro.
    Para spin ~ 1, la eficiencia máxima es ~29%.
    """
    if spin < 0 or spin > 1:
        raise ValueError("Spin debe estar entre 0 y 1.")
    return 0.29 * spin

energy_mass_equiv = 9e16  # J/kg (E=mc^2 approx)

mass_bh = 1e3  # kg (mini agujero negro hipotético)
spin_bh = 0.8

efficiency = penrose_extraction_efficiency(spin_bh)
energy_available = mass_bh * energy_mass_equiv * efficiency

print(f"Energía disponible para propulsión: {energy_available:.2e} J")
