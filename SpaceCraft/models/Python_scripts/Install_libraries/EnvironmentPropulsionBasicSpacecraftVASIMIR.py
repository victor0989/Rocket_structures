def relativistic_time_dilation(gravity, r, c=3e8):
    """Tiempo propio afectado por gravedad fuerte (magnetar, Sagitario A*)"""
    rs = 2 * gravity * 6.674e-11 / c**2  # radio de Schwarzschild
    if r <= rs:
        return 0  # dentro del horizonte
    return math.sqrt(1 - rs / r)

def vasimr_efficiency(temp_K, B_Tesla):
    """Eficiencia simplificada del motor VASIMR"""
    return min((B_Tesla * math.log(temp_K)) / 100, 1)

# Ejemplo de simulación
gravity_mass = 4e30  # Sagitario A*
distance = 1e8  # metros
print(f"Time Dilation Factor: {relativistic_time_dilation(gravity_mass, distance)}")

temp = 120000
B = 4.2
print(f"VASIMR Efficiency: {vasimr_efficiency(temp, B)}")
