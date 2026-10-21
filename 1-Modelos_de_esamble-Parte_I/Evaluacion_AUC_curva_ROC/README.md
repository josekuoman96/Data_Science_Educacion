# Evaluación del AUC y la curva ROC

**Autor:** José Ignacio Kuoman Jiménez · **Generación:** G83 · **Módulo:** Modelos de ensamble (Parte I)

**Archivo:** `evaluación del AUC y la curva ROC.ipynb` · **Datos:** `load_breast_cancer` de scikit-learn

## Objetivo

Aprender a evaluar un clasificador con la **curva ROC** y el **AUC**, y a usar las probabilidades predichas para priorizar casos.

## Qué hace el código

1. Carga el dataset de cáncer de mama, separa train/test y estandariza los datos.
2. Entrena una **Regresión Logística** y obtiene las probabilidades de la clase positiva.
3. Calcula la curva ROC y el AUC, y las grafica.
4. Ordena las probabilidades y muestra las **15 personas con mayor probabilidad**. Es la misma técnica que se usa después en el Desafío 1 para los clientes en riesgo.

---

[← Volver al índice](../README.md)
