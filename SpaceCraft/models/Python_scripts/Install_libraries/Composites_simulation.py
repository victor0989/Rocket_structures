import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample carbon fiber dataset (simplified, you can expand this)
data = [
    # Manufacturer, Model, Type, Tensile (GPa), Modulus (GPa), Strain (%), Density (g/cm³)
    ['Amoco', 'T-50', 'PAN', 2.90, 300, 1.61, 1.81],
    ['Amoco', 'T-40', 'PAN', 5.65, 290, 1.88, 1.81],
    ['BASF', 'Celion GY-70', 'PAN', 8.4, 186, 0.30, 1.90],
    ['Grafil', '34-700', 'PAN', 4.5, 234, 1.9, 1.80],
    ['Hercules', 'IM6', 'PAN', 5.1, 303, 1.7, 1.74],
    ['Toray', 'M40J', 'PAN', 4.41, 377, 1.2, 1.79],
    ['Toray', 'M60J', 'PAN', 3.90, 588, 0.9, 1.93],
    ['Amoco', 'P-120', 'Pitch', 2.37, 827, 0.30, 2.18],
    ['DuPont', 'G-E120', 'Pitch', 3.10, 827, 0.48, 2.14],
    ['Mitsubishi', 'NT-60', 'Pitch', 3.0, 595, 0.7, 2.10],
]

df = pd.DataFrame(data, columns=[
    "Manufacturer", "Model", "Type", "Tensile Strength (GPa)",
    "Young's Modulus (GPa)", "Strain (%)", "Density (g/cm³)"
])

# Save table as image (optional)
def save_table(df, filename="carbon_fibers_table.png"):
    fig, ax = plt.subplots(figsize=(18, len(df) * 0.6))
    ax.axis("off")
    table = ax.table(cellText=df.values,
                     colLabels=df.columns,
                     loc='center',
                     cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.5)
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Table saved as {filename}")

save_table(df)

# Plot comparison of Tensile Strength vs. Strain
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x="Strain (%)", y="Tensile Strength (GPa)", hue="Type", style="Manufacturer", s=150)
plt.title("Tensile Strength vs. Strain (%) by Fiber Type")
plt.xlabel("Strain (%)")
plt.ylabel("Tensile Strength (GPa)")
plt.grid(True)
plt.tight_layout()
plt.savefig("tensile_vs_strain.png", dpi=300)
#plt.show()
