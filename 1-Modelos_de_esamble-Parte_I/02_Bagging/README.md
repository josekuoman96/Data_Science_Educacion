# 02 - Bagging

**Autor:** José Ignacio Kuoman Jiménez · **Generación:** G83 · **Módulo:** Modelos de ensamble (Parte I)

**Archivo:** `02 - Bagging.ipynb` · **Datos:** `insurance.csv`, `ObesityDataSet.csv`

## Objetivo

Entender cómo funciona el ensamble **Bagging**: cómo mejora al aumentar el número de estimadores, cuál es su principal debilidad (la alta correlación entre sus árboles) y cómo se puede usar con **modelos heterogéneos**.

## Qué hace el código

1. Entrena un `BaggingRegressor` para predecir el costo de seguros médicos (`charges`) y lo evalúa con R² y RMSE (≈82 % de varianza explicada en test).
2. Prueba distintas cantidades de árboles (de 10 a 1000) y muestra que, desde unos 300, agregar más ya no mejora el modelo.
3. Grafica la predicción de cada árbol para una observación concreta y calcula la **correlación entre los árboles** (todas mayores a 0.88), lo que motiva el uso de Random Forest.
4. Con el dataset de obesidad, aplica un **Bagging heterogéneo** (árbol, SVM y regresión logística) usando `util_bagging.py`, cambiando el peso de cada modelo en la bolsa.

---

[← Volver al índice](../README.md)
