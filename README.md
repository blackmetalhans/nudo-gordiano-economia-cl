# El Nudo Gordiano de la Economía Chilena

[![Executable Paper](https://img.shields.io/badge/Paper-Executable-blue.svg)](https://blackmetalhans.github.io/nudo-gordiano-economia-cl/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Ejecutable Paper:** Modelado estocástico de ineficiencias estructurales y pérdida de bienestar agregado.

## 1. Executive Summary
Este repositorio cuantifica matemáticamente la histéresis del desarrollo en Chile, modelando el colapso de la Productividad Total de Factores (PTF) desde la perspectiva del ingreso neto ciudadano ($I_{neto}$). El modelo abandona el análisis discursivo tradicional para plantear un sistema de ecuaciones estocásticas calibrables y auditables en tiempo real.

## 2. Ecuación Fundamental de Bienestar

$$I_{neto,t} = \underbrace{Y_0 \cdot \mathcal{E}(k)}_{\text{Rendimiento Base}} - \underbrace{\delta_E(\beta+\tau)}_{\text{Fricción Energética}} - \underbrace{\delta_C\mu_{m^2}^{eff}}_{\text{Exacción Inmob.}} - \underbrace{\phi B_t}_{\text{Shock Externo}} + \eta_t$$

---

## Índice de Navegación
* [🛠️ Infraestructura de Automatización (Live Engine)](#🛠️-infraestructura-de-automatización-(live-engine))

---

## 🛠️ Infraestructura de Automatización (Live Engine)
Este paper se recalibra dinámicamente utilizando el siguiente stack:
- **Motor de Ingesta**: `src/fetch_data.py` - Captura semanal de UF, UTM e IPC para ajuste de base monetaria simulada.
- **Simulador Dinámico**: `src/simulador.py` - Motor de Monte Carlo que integra `data/live_indicators.json` para proyecciones de estrés financiero.
- **Visualización**: Dashboard brutalista en `index.html` con inyección de datos en tiempo real.