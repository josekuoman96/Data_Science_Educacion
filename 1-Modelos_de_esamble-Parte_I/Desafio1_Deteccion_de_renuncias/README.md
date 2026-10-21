# Desafío 1 – Detección temprana de renuncias en empresas de telecomunicaciones

**Autor:** José Ignacio Kuoman Jiménez · **Generación:** G83 · **Módulo:** Modelos de ensamble (Parte I)

**Archivos:** `Desafio1-Deteccion_temprana_de_renuncias_en_empresas_de_telecomunicaciones-Jose_Kuoman_Jimenez.ipynb` y `Desafio_1-...ipynb` (dos versiones del mismo desafío) · **Datos:** `telecom_churn.csv`

## Objetivo

Las empresas de telefonía compiten fuertemente por sus clientes, y retener a uno antiguo cuesta menos que conseguir uno nuevo. El objetivo de este desafío es **entrenar modelos de ensamble capaces de predecir de forma temprana si un cliente renunciará a la compañía (churn)** y **explicar qué características influyen más** en que un cliente se vaya o se quede.

## Qué hace el código

1. **Análisis exploratorio:** distribución de cada variable, detección de outliers con boxplots (IQR) y un heatmap de correlaciones.
2. **Árbol de decisión:** un modelo base sin ajustar y luego uno optimizado con `GridSearchCV` (5-fold) sobre `max_depth` y `min_samples_split` para reducir el overfitting.
3. **SMOTE + Bagging:** balancea las clases del conjunto de entrenamiento y entrena un `BaggingClassifier` con 200 árboles.
4. **Bagging heterogéneo:** combina Regresión Logística, Árbol de decisión y SVM (kernels `rbf` y `sigmoid`) con 200 muestras bootstrap y repite el modelo con mejor F1-score (usa `util_bagging.py`).
5. **Random Forest (45 árboles):** estima el accuracy con la muestra OOB y muestra las 4 variables más importantes.
6. **Random Forest optimizado:** búsqueda de grilla sobre `n_estimators` (50–190) y `max_features`, con evaluación OOB, curva ROC y AUC.
7. **Clientes en riesgo:** con el mejor Random Forest, lista los 15 clientes con mayor probabilidad de renunciar.

## Principales conclusiones

- Las variables con más peso para predecir la renuncia son **DayMins, MonthlyCharge, CustServCalls y OverageFee**.
- El Random Forest ajustado obtiene un **AUC superior a 0.9**, por lo que es el modelo más adecuado para detectar clientes en riesgo de irse.

---

[← Volver al índice](../README.md)
