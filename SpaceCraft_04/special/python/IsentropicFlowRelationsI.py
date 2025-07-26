import math

# Constants for air (ideal gas) at room temperature
k = 1.4           # Specific heat ratio (Cp/Cv)
R = 287.0         # Specific gas constant for air, J/(kg·K)
cp = k * R / (k - 1)  # Specific heat at constant pressure, J/(kg·K)

def stagnation_temperature(T, v):
    """
    Calculate stagnation temperature T0 given static temperature T (K)
    and flow velocity v (m/s).
    Eq: T0 = T + v^2 / (2 * cp)
    """
    T0 = T + v**2 / (2 * cp)
    return T0

def stagnation_pressure(p, T, T0):
    """
    Calculate stagnation pressure p0 given static pressure p,
    static temperature T, and stagnation temperature T0.
    Eq: p0/p = (T0/T)^(k/(k-1))
    """
    pressure_ratio = (T0 / T) ** (k / (k - 1))
    p0 = p * pressure_ratio
    return p0

def speed_of_sound(T):
    """
    Calculate the speed of sound a given static temperature T (K).
    Eq: a = sqrt(k * R * T)
    """
    a = math.sqrt(k * R * T)
    return a

def mach_number(v, T):
    """
    Calculate Mach number M given velocity v (m/s) and static temperature T (K).
    Eq: M = v / a
    """
    a = speed_of_sound(T)
    M = v / a
    return M

# Example values
static_temp = 300.0  # K (about 27°C)
static_pressure = 101325.0  # Pa (sea level atmospheric pressure)
velocity = 100.0  # m/s (flow velocity)

# Calculate stagnation properties
T0 = stagnation_temperature(static_temp, velocity)
p0 = stagnation_pressure(static_pressure, static_temp, T0)
a = speed_of_sound(static_temp)
M = mach_number(velocity, static_temp)

print(f"Static Temperature (T): {static_temp} K")
print(f"Velocity (v): {velocity} m/s")
print(f"Stagnation Temperature (T0): {T0:.2f} K")
print(f"Static Pressure (p): {static_pressure} Pa")
print(f"Stagnation Pressure (p0): {p0:.2f} Pa")
print(f"Speed of Sound (a): {a:.2f} m/s")
print(f"Mach Number (M): {M:.3f}")
