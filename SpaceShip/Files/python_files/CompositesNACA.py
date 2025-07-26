import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

data = [
    # Manufacturer, Name, Tensile Strength (GPa), Density (g/cm³), Young Modulus (GPa),
    # Strain (%), Electrical Resistivity (µΩ.m), Note
    ["Amoco", "T-50", 6.5, 1.81, 2.90, 300, "0.7 / 1.61–4.09", "Calculated"],
    ["Amoco", "T-40", 5.1, 1.81, 5.65, 290, "1.8 / 1.88–2.7", "Calculated"],
    ["BASF", "Celion Gy-70", 8.4, 1.90, 1.86, 517, "0.30 / 1.05", "Calculated"],
    ["Grafil", "Grafil 34-700", 6.9, 1.80, 4.50, 234, "1.9 / 2.76", "Calculated"],
    ["Hercules", "Magnamite IM6", 5.4, 1.74, 5.10, 303, "1.7 / 2.8–7.1", "Calculated"],
    ["Toray", "Torayca T800H", 5.0, 1.81, 5.49, 294, "1.9 / 2.74–7.86", "Calculated"],
    ["Amoco", "Thornel P-120", 10.0, 2.18, 2.37, 827, "0.3 / 0.30–0.40", "Calculated"],
    ["DuPont", "FiberG-E105", 9.3, 2.14, 3.10, 717, "0.5 / 0.74", "Measured"],
    ["Mitsubishi", "NT-60", "9.4–3.0", "", 595, "", "0.8–1.8 / 0.7", "Calculated"],
]

columns = ["Manufacturer", "Name", "Tensile Strength (GPa)", "Density (g/cm³)",
           "Young's Modulus (GPa)", "Strain (MPa)", "Resistivity (µΩ·m)", "Note"]

df = pd.DataFrame(data, columns=columns)

# Setup matplotlib font to Courier New
font_path = fm.findfont(fm.FontProperties(family='Courier New'))
prop = fm.FontProperties(fname=font_path)

# Plot table
fig, ax = plt.subplots(figsize=(18, len(df) * 0.7))
ax.axis("off")
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 loc="center",
                 cellLoc='center',
                 colLoc='center',
                 colColours=["#cce6ff"] * len(columns))

table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)

# Save as PNG
plt.tight_layout()
plt.savefig("carbon_fiber_compounds_table.png", dpi=300, bbox_inches="tight")
print("Table saved as carbon_fiber_compounds_table.png")
