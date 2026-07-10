# **El Nudo Gordiano de la Economía Chilena**

[![Executable Paper](https://img.shields.io/badge/Paper-Executable-blue.svg)](https://blackmetalhans.github.io/nudo-gordiano-economia-cl/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Modelado Estocástico de Ineficiencias Estructurales y Pérdida de Bienestar Agregado**

Este repositorio constituye un **Executable Paper**. Cuantifica la histéresis del desarrollo en Chile mediante un sistema de ecuaciones estocásticas calibrables.

## **1. Marco Teórico**

$$I_{neto,t} = \underbrace{Y_0 \cdot \mathcal{E}(k)}_{\text{Rendimiento Base}} - \underbrace{\delta_E(\beta+\tau)}_{\text{Fricción Energética}} - \underbrace{\delta_C\mu_{m^2}^{eff}}_{\text{Exacción Inmob.}} - \underbrace{\phi B_t}_{\text{Shock Externo}} + \eta_t$$

## **2. Funcionamiento y Ejecución**

Este proyecto está diseñado para ejecutarse en entornos de Python 3.10+ o Google Colab.

### **Instalación**
```bash
git clone https://github.com/blackmetalhans/nudo-gordiano-economia-cl.git
cd nudo-gordiano-economia-cl
pip install -r requirements.txt
```

### **Uso del Modelo**
Para replicar las simulaciones de Monte Carlo y generar los datasets de bienestar:
```python
from src.modelo import simulador_estocastico

# Ejecutar simulación con 10,000 iteraciones
resultados = simulador_estocastico(iteraciones=10000)
display(resultados.head())
```

## **3. Metodología**
El modelo utiliza simulaciones para proyectar trayectorias de crecimiento bajo escenarios de estrés institucional. La calibración se basa en series históricas de precios de energía y avalúos inmobiliarios.

## **4. Conclusiones**
La economía chilena presenta un 'techo de cristal' determinado por costos fijos institucionales que drenan el ingreso neto ciudadano.

---
*Nota: Documentación completa restaurada con guía de funcionamiento.*