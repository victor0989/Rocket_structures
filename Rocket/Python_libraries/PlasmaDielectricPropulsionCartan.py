# This script simulates a conceptual quantum propulsion system combining:
# - Blade loading/flow/reaction coefficients from turbine theory
# - Plasma dielectric behavior under magnetic fields
# - Cartan geometric field theory for advanced propulsion
# - Turboshaft energy partitioning
# It integrates physics and engineering theories under a unifying Python model

import numpy as np
import matplotlib.pyplot as plt

# --- Constants ---
Cp = 1004                        # Specific heat at constant pressure [J/kg·K] (air)
ε0 = 8.854e-12                   # Vacuum permittivity [F/m]
μ0 = 4 * np.pi * 1e-7           # Vacuum permeability [H/m]
c = 3e8                          # Speed of light [m/s]
m_p = 1.67e-27                   # Proton mass [kg]
q_e = 1.6e-19                    # Elementary charge [C]

# --- Plasma and field parameters ---
B = 0.1                          # Magnetic field [T]
n = 1e16                         # Particle density [1/m^3]
ρ = n * m_p                      # Mass density [kg/m^3]
εR = 1 + (μ0 * ρ * c**2) / (B**2)  # Effective dielectric constant

# --- Flow mechanics (compressor stage) ---
U = 300                          # Blade speed [m/s]
Ca = 150                         # Axial velocity [m/s]
alpha2, alpha3 = np.radians(45), np.radians(30)
beta2, beta3 = np.radians(60), np.radians(20)

# Flow and loading coefficients
phi = Ca / U                    # Eq. (10.12)
psi_a = 2 * phi * (np.tan(alpha2) + np.tan(alpha3))   # Eq. (10.11b) alpha
psi_b = 2 * phi * (np.tan(beta2) + np.tan(beta3))     # Eq. (10.11b) beta

# --- Degree of reaction from beta angles (Eq. 10.13d) ---
Lambda = (phi / 2) * (np.tan(beta3)**2 - np.tan(beta2)**2)

# --- Lorentz Force Simulation (single ion) ---
def lorentz_accel(q, m, E, B, u):
    return (q / m) * (E + np.cross(u, B))

# Ion simulation setup
q_s = q_e
m_s = m_p
E_field = np.array([0, 1e3, 0])       # Electric field [V/m]
B_field = np.array([0, 0, B])         # Magnetic field [T]
velocity = np.array([1e3, 0, 0])      # Initial velocity [m/s]

# Time evolution (1 ms)
dt = 1e-6
steps = 1000
positions = [np.array([0.0, 0.0, 0.0])]
velocities = [velocity.copy()]

for _ in range(steps):
    a = lorentz_accel(q_s, m_s, E_field, B_field, velocities[-1])
    new_v = velocities[-1] + a * dt
    new_p = positions[-1] + new_v * dt
    velocities.append(new_v)
    positions.append(new_p)

positions = np.array(positions)

# --- Display Outputs ---
print(f"Effective Plasma Dielectric Constant εR: {εR:.3e}")
print(f"Flow Coefficient ϕ: {phi:.3f}")
print(f"Blade Loading Coefficient ψ (alpha): {psi_a:.3f}")
print(f"Blade Loading Coefficient ψ (beta): {psi_b:.3f}")
print(f"Degree of Reaction Λ: {Lambda:.3f}")

# --- Plot ion trajectory ---
plt.figure(figsize=(10, 5))
plt.plot(positions[:, 0], positions[:, 1], label="Ion Trajectory")
plt.xlabel("X [m]")
plt.ylabel("Y [m]")
plt.title("Ion Trajectory Under Lorentz Force")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
