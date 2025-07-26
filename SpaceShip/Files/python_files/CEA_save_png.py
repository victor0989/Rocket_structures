import matplotlib.pyplot as plt
import numpy as np

# Simulación de un gráfico representativo de los datos termodinámicos
temperatures = np.linspace(2000, 5000, 100)
gamma_values = 1.2 + 0.2 * np.sin(temperatures / 1000)  # valores ficticios para gamma

plt.figure(figsize=(10, 6))
plt.plot(temperatures, gamma_values, label='Gamma (Cp/Cv)', color='blue')
plt.title('Relación de calores específicos ($\gamma$) vs Temperatura')
plt.xlabel('Temperatura [K]')
plt.ylabel('Gamma ($\gamma$)')
plt.grid(True)
plt.legend()

# Guardar como imagen PNG
output_path = "/mnt/data/cea_gamma_vs_temperature.png"
plt.savefig(output_path, format="png")
output_path
