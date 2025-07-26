import math


def fluidez_metal(viscosidad, sensibilidad_visc, tension_superficial, inclusiones,
                  intervalo_solidificacion, conductividad_molde, rugosidad_molde,
                  sobrecalentamiento, velocidad_vaciado):
    """
    Calcula un índice simplificado de fluidez del metal fundido.

    Parámetros:
    - viscosidad: viscosidad base del metal fundido (Pa·s)
    - sensibilidad_visc: índice de sensibilidad de la viscosidad a temperatura (adimensional)
    - tension_superficial: tensión superficial del metal fundido (N/m)
    - inclusiones: factor de inclusiones (0 a 1, donde 0=no inclusiones, 1=muchas)
    - intervalo_solidificacion: intervalo de solidificación (°C)
    - conductividad_molde: conductividad térmica del molde (W/m·K)
    - rugosidad_molde: rugosidad del molde (adimensional, 0=liso, >0 rugoso)
    - sobrecalentamiento: grado de sobrecalentamiento (°C)
    - velocidad_vaciado: velocidad de vaciado (m/s)

    Retorna:
    - índice de fluidez (mayor valor indica mejor fluidez)
    """

    # Factor viscosidad (mayor viscosidad y sensibilidad disminuyen fluidez)
    f_visc = 1 / (viscosidad * (1 + sensibilidad_visc))

    # Factor tensión superficial (mayor tensión reduce fluidez)
    f_tension = 1 / (1 + tension_superficial)

    # Factor inclusiones (mayor inclusiones reducen fluidez)
    f_inclusiones = 1 - inclusiones  # suponer inclusiones en 0..1

    # Factor intervalo solidificación (fluidez inversamente proporcional al intervalo)
    f_solid = 1 / intervalo_solidificacion

    # Factor conductividad y rugosidad del molde (mayor conductividad y rugosidad reducen fluidez)
    f_molde = 1 / (1 + conductividad_molde * rugosidad_molde)

    # Factor sobrecalentamiento (mayor sobrecalentamiento mejora fluidez)
    f_sobre = 1 + 0.05 * sobrecalentamiento

    # Factor velocidad de vaciado (mayor velocidad mejora fluidez)
    f_vel = velocidad_vaciado

    # Índice global multiplicativo
    indice_fluidez = f_visc * f_tension * f_inclusiones * f_solid * f_molde * f_sobre * f_vel

    return indice_fluidez


# Ejemplo de uso
if __name__ == "__main__":
    indice = fluidez_metal(
        viscosidad=0.005,  # Pa·s
        sensibilidad_visc=0.2,  # adimensional
        tension_superficial=1.0,  # N/m
        inclusiones=0.1,  # 10% inclusiones
        intervalo_solidificacion=10,  # °C
        conductividad_molde=30,  # W/m·K (ej. molde de acero)
        rugosidad_molde=0.3,  # adimensional
        sobrecalentamiento=50,  # °C
        velocidad_vaciado=1.2  # m/s
    )

    print(f"Índice de fluidez calculado: {indice:.4f}")
