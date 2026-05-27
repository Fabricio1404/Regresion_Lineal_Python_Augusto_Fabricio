# 📊 TP2 – Estadística: Regresión Lineal y Correlación

Trabajo Práctico N°2 de Estadística – Instituto Politécnico Formosa  
Análisis de regresión lineal y correlación sobre dos conjuntos de datos reales.

---

## 📁 Estructura del proyecto

```
TP2_Estadistica/
│
├── main.py          # Código principal con ambos casos
└── README.md        # Este archivo
```

---

## 📌 Casos analizados

### Caso 1 — Tiempo vs Altura del agua 💧
Se analiza cómo varía la altura del agua en un depósito cilíndrico a medida que pasa el tiempo.

| Variable | Descripción |
|----------|-------------|
| **Independiente (x)** | Tiempo transcurrido (horas) |
| **Dependiente (y)** | Altura del agua (metros) |

**Resultados:**
- Ecuación de regresión: `y = 18.99 − 0.252x`
- Coeficiente de correlación: `r = −0.9969` (negativa muy fuerte)
- Coeficiente de determinación: `r² = 99.39%`

### Caso 2 — Horas de estudio vs Calificación 📚
Se analiza si existe relación entre las horas de estudio declaradas por los alumnos y su calificación en el examen de ingreso del IPF.

| Variable | Descripción |
|----------|-------------|
| **Independiente (x)** | Cantidad de horas de estudio |
| **Dependiente (y)** | Calificación obtenida |

**Resultados:**
- Ecuación de regresión: `y = 1.6579 + 0.0131x`
- Coeficiente de correlación: `r = 0.8404` (positiva fuerte)
- Coeficiente de determinación: `r² = 70.62%`

---

## 🛠️ Tecnologías utilizadas

- **Python 3**
- **pandas** — manejo de datos y tablas
- **NumPy** — cálculos matemáticos
- **Matplotlib** — gráficos de dispersión y recta de regresión

---

## ▶️ Cómo ejecutar

1. Clonar el repositorio:
```bash
git clone https://github.com/Fabricio1404/Regresion_Lineal_Python_Augusto_Fabricio.git
cd Regresion_Lineal_Python_Augusto_Fabricio
```

2. Instalar las dependencias:
```bash
pip install pandas numpy matplotlib
```

3. Ejecutar el script:
```bash
python main.py
```

---

## 📈 Qué muestra el programa

Para cada caso, el programa:

1. Muestra los datos de entrada (arrays)
2. Genera la tabla de cálculos con columnas `x*y`, `x²`, `y²`
3. Calcula las sumatorias `∑x`, `∑y`, `∑xy`, `∑x²`, `∑y²`
4. Obtiene la ecuación de la recta de regresión (`a` y `b`)
5. Calcula el coeficiente de correlación `r` y el de determinación `r²`
6. Genera un gráfico de dispersión con la recta de regresión

---

## 🏫 Información académica

| | |
|---|---|
| **Institución** | Instituto Politécnico Formosa (IPF) |
| **Materia** | Estadística |
| **Trabajo** | Práctico N°2 |
| **Tema** | Regresión Lineal y Correlación |