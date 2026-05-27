import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==============================================================
#   TRABAJO PRÁCTICO II – ESTADÍSTICA
#   Regresión Lineal y Correlación
# ==============================================================

# ──────────────────────────────────────────────────────────────
#  CASO 1: Tiempo (h) vs Altura (m) — Depósito cilíndrico
# ──────────────────────────────────────────────────────────────

print("=" * 60)
print("  CASO 1: TIEMPO (h) vs ALTURA DEL AGUA (m)")
print("=" * 60)

# 1) DATOS
# Variable independiente (x): Tiempo en horas
tiempo = [8, 14, 22, 27, 33, 50, 60]

# Variable dependiente (y): Altura del agua en metros
altura = [17, 15, 14, 12, 11, 6, 4]

print("\n1) DATOS\n")
print("Variable independiente (x): Tiempo (h)")
print("Variable dependiente   (y): Altura del agua (m)")
print("\nTiempo:", tiempo)
print("Altura:", altura)

# 2) TABLA DE CÁLCULOS
df1 = pd.DataFrame({
    "Tiempo": tiempo,
    "Altura": altura
})

df1["x*y"]  = df1["Tiempo"] * df1["Altura"]
df1["x^2"]  = df1["Tiempo"] ** 2
df1["y^2"]  = df1["Altura"] ** 2

print("\n2) TABLA DE CÁLCULOS\n")
print(df1.to_string(index=False))

# 3) SUMATORIAS
n1            = len(df1)
sum_x1        = df1["Tiempo"].sum()
sum_y1        = df1["Altura"].sum()
sum_xy1       = df1["x*y"].sum()
sum_x2_1      = df1["x^2"].sum()
sum_y2_1      = df1["y^2"].sum()

print("\n3) SUMATORIAS\n")
print(f"  n      = {n1}")
print(f"  ∑x     = {sum_x1}")
print(f"  ∑y     = {sum_y1}")
print(f"  ∑xy    = {sum_xy1}")
print(f"  ∑x²    = {sum_x2_1}")
print(f"  ∑y²    = {sum_y2_1}")

# 4) REGRESIÓN LINEAL
b1 = ((n1 * sum_xy1) - (sum_x1 * sum_y1)) / ((n1 * sum_x2_1) - (sum_x1 ** 2))
a1 = ((sum_y1 * sum_x2_1) - (sum_xy1 * sum_x1)) / ((n1 * sum_x2_1) - (sum_x1 ** 2))

print("\n4) REGRESIÓN LINEAL\n")
print(f"  Pendiente  b = {b1:.4f}")
print(f"  Ordenada   a = {a1:.4f}")
print(f"\n  Ecuación de la recta: y = {a1:.4f} + ({b1:.4f})x")

# 5) CORRELACIÓN
r1  = ((n1 * sum_xy1) - (sum_x1 * sum_y1)) / \
      np.sqrt(((n1 * sum_x2_1) - (sum_x1 ** 2)) * ((n1 * sum_y2_1) - (sum_y1 ** 2)))
r2_1 = r1 ** 2

print("\n5) CORRELACIÓN\n")
print(f"  r   = {r1:.4f}")
print(f"  r²  = {r2_1:.4f}")

if r1 > 0:
    print("\n  La correlación es POSITIVA.")
elif r1 < 0:
    print("\n  La correlación es NEGATIVA.")
else:
    print("\n  No existe correlación.")

print(f"  El modelo explica aproximadamente el {r2_1 * 100:.2f}% de la variabilidad.")

# 6) GRÁFICO
x_linea1 = np.linspace(min(tiempo), max(tiempo), 100)
y_linea1 = a1 + b1 * x_linea1

plt.figure(figsize=(8, 5))
plt.scatter(tiempo, altura, color="steelblue", zorder=5, label="Datos observados")
plt.plot(x_linea1, y_linea1, color="tomato", label=f"Recta: y = {a1:.2f} + ({b1:.2f})x")
plt.title("Regresión Lineal – Tiempo vs Altura del agua")
plt.xlabel("Tiempo (h)")
plt.ylabel("Altura (m)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()


# ──────────────────────────────────────────────────────────────
#  CASO 2: Horas de estudio vs Calificación
# ──────────────────────────────────────────────────────────────

print("\n" + "=" * 60)
print("  CASO 2: HORAS DE ESTUDIO vs CALIFICACIÓN")
print("=" * 60)

# 1) DATOS
# Variable independiente (x): Cantidad de horas de estudio
horas = [120.2, 133.5, 548.9, 254.6, 147.2, 178.0, 426.5, 450.0, 355.7, 756.7, 351.3]

# Variable dependiente (y): Calificación obtenida
calificacion = [2, 4, 9, 6, 1, 3, 10, 8, 7, 9, 8]

print("\n1) DATOS\n")
print("Variable independiente (x): Horas de estudio")
print("Variable dependiente   (y): Calificación")
print("\nHoras:", horas)
print("Calificación:", calificacion)

# 2) TABLA DE CÁLCULOS
df2 = pd.DataFrame({
    "Horas de estudio": horas,
    "Calificación": calificacion
})

df2["x*y"]  = df2["Horas de estudio"] * df2["Calificación"]
df2["x^2"]  = df2["Horas de estudio"] ** 2
df2["y^2"]  = df2["Calificación"] ** 2

print("\n2) TABLA DE CÁLCULOS\n")
print(df2.to_string(index=False))

# 3) SUMATORIAS
n2            = len(df2)
sum_x2        = df2["Horas de estudio"].sum()
sum_y2        = df2["Calificación"].sum()
sum_xy2       = df2["x*y"].sum()
sum_x2_2      = df2["x^2"].sum()
sum_y2_2      = df2["y^2"].sum()

print("\n3) SUMATORIAS\n")
print(f"  n      = {n2}")
print(f"  ∑x     = {sum_x2:.2f}")
print(f"  ∑y     = {sum_y2}")
print(f"  ∑xy    = {sum_xy2:.2f}")
print(f"  ∑x²    = {sum_x2_2:.2f}")
print(f"  ∑y²    = {sum_y2_2}")

# 4) REGRESIÓN LINEAL
b2 = ((n2 * sum_xy2) - (sum_x2 * sum_y2)) / ((n2 * sum_x2_2) - (sum_x2 ** 2))
a2 = ((sum_y2 * sum_x2_2) - (sum_xy2 * sum_x2)) / ((n2 * sum_x2_2) - (sum_x2 ** 2))

print("\n4) REGRESIÓN LINEAL\n")
print(f"  Pendiente  b = {b2:.4f}")
print(f"  Ordenada   a = {a2:.4f}")
print(f"\n  Ecuación de la recta: y = {a2:.4f} + {b2:.4f}x")

# 5) CORRELACIÓN
r2  = ((n2 * sum_xy2) - (sum_x2 * sum_y2)) / \
      np.sqrt(((n2 * sum_x2_2) - (sum_x2 ** 2)) * ((n2 * sum_y2_2) - (sum_y2 ** 2)))
r2_2 = r2 ** 2

print("\n5) CORRELACIÓN\n")
print(f"  r   = {r2:.4f}")
print(f"  r²  = {r2_2:.4f}")

if r2 > 0:
    print("\n  La correlación es POSITIVA.")
elif r2 < 0:
    print("\n  La correlación es NEGATIVA.")
else:
    print("\n  No existe correlación.")

print(f"  El modelo explica aproximadamente el {r2_2 * 100:.2f}% de la variabilidad.")

# 6) GRÁFICO
x_linea2 = np.linspace(min(horas), max(horas), 100)
y_linea2 = a2 + b2 * x_linea2

plt.figure(figsize=(8, 5))
plt.scatter(horas, calificacion, color="steelblue", zorder=5, label="Datos observados")
plt.plot(x_linea2, y_linea2, color="tomato", label=f"Recta: y = {a2:.4f} + {b2:.4f}x")
plt.title("Regresión Lineal – Horas de estudio vs Calificación")
plt.xlabel("Horas de estudio")
plt.ylabel("Calificación")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
