# 02 - RandomForest

**Autor:** José Ignacio Kuoman Jiménez · **Generación:** G83 · **Módulo:** Modelos de ensamble (Parte I)

**Archivo:** `02 - RandomForest.ipynb` · **Datos:** `diabetes_prediction_dataset.csv`

## Objetivo

Aplicar **Random Forest** a un problema de clasificación desbalanceado (predecir diabetes) e interpretar qué variables pesan más en la predicción.

## Qué hace el código

1. Explora los datos y observa el desbalance de la variable objetivo.
2. Convierte las variables categóricas en dummies y separa train/test.
3. Entrena un `RandomForestClassifier` con `class_weight='balanced'` para compensar el desbalance y muestra el reporte de clasificación.
4. Grafica la **importancia de atributos**: HbA1c y glucosa en sangre son las más importantes, seguidas de edad e IMC.
5. Compara el error OOB y de test para distintas cantidades de árboles y valores de `max_features` (`None`, `sqrt`, `log2`). `sqrt` y `log2` dan menor error.

---

[← Volver al índice](README.md)
