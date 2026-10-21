# Random_Forest-11_09_2024

**Autor:** José Ignacio Kuoman Jiménez · **Generación:** G83 · **Módulo:** Modelos de ensamble (Parte I)

**Archivo:** `Random_Forest-11_09_2024.ipynb` · **Datos:** UCI (descargados con `ucimlrepo`): *Concrete Compressive Strength* y *Early Stage Diabetes Risk Prediction*

## Objetivo

Mostrar por qué **Random Forest es más estable y sufre menos overfitting** que un solo árbol de decisión, y cómo usar la importancia de variables, SMOTE y el **Stacking**.

## Qué hace el código

1. **Regresión (resistencia del concreto):** repite 100 veces la división train/test y compara con boxplots el R², MAE y MAPE de un árbol frente a un Random Forest, primero con los datos originales y luego con ruido añadido. El árbol varía mucho más.
2. **Importancia de variables:** identifica `Cement` y `Age` como las más importantes y muestra cómo cambia el R² al quitar o dejar solo ciertas variables.
3. **Clasificación (riesgo de diabetes):** binariza las variables, entrena un árbol con `GridSearchCV` y luego un Random Forest con datos balanceados con **SMOTE**, comparando la matriz de confusión, el accuracy y el F1.
4. **Stacking:** combina árbol, dos SVM y regresión logística en un `StackingClassifier`.

---

[← Volver al índice](../README.md)
