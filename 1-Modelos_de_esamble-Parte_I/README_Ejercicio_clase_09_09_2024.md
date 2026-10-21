# Ejercicio clase - Modelos de ensamble (Parte I) - 09_09_2024

**Autor:** José Ignacio Kuoman Jiménez · **Generación:** G83 · **Módulo:** Modelos de ensamble (Parte I)

**Archivo:** `Ejercicio clase - Modelos de ensamble (Parte I) - 09_09_2024.ipynb` · **Datos:** `boston.csv`

## Objetivo

Comparar un **árbol de decisión**, **Bagging** y **Random Forest** para predecir el valor mediano de las viviendas en Boston (`MEDV`).

## Qué hace el código

1. Revisa los datos y los valores nulos, y separa train/test.
2. Entrena un `DecisionTreeRegressor`, lo evalúa con R² y MSE (≈63 % de varianza explicada) y muestra la importancia de las variables (RM, LSTAT, DIS).
3. Entrena un `BaggingRegressor` con 100 árboles y estima R² con los datos **OOB**.
4. Entrena un `RandomForestRegressor`, estima R² OOB y vuelve a calcular la importancia (RM, LSTAT, CRIM).
5. Ajusta los hiperparámetros del Random Forest con `GridSearchCV` y usa el mejor modelo para predecir el precio de una vivienda en particular.

---

[← Volver al índice](README.md)
