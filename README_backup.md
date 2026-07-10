# El Nudo Gordiano de la Economía Chilena

[![Executable Paper](https://img.shields.io/badge/Paper-Executable-blue.svg)](https://blackmetalhans.github.io/nudo-gordiano-economia-cl/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Ejecutable Paper:** Modelado estocástico de ineficiencias estructurales y pérdida de bienestar agregado.

## 1. Executive Summary
Este repositorio cuantifica matemáticamente la histéresis del desarrollo en Chile, modelando el colapso de la Productividad Total de Factores (PTF) desde la perspectiva del ingreso neto ciudadano ($I_{neto}$). El modelo abandona el análisis discursivo tradicional para plantear un sistema de ecuaciones estocásticas calibrables y auditables en tiempo real.

## 2. Quick Start
```bash
git clone https://github.com/blackmetalhans/nudo-gordiano-economia-cl.git
cd nudo-gordiano-economia-cl
```

## 3. Framework Teórico (Los 4 Pilares)

La ecuación fundamental de transferencia de bienestar:

$$I_{neto,t} = \underbrace{Y_0 \cdot \mathcal{E}(k)}_{\text{Rendimiento Base}} - \underbrace{\delta_E(\beta+\tau)}_{\text{Fricción Energética}} - \underbrace{\delta_C\mu_{m^2}^{eff}}_{\text{Exacción Inmob.}} - \underbrace{\phi B_t}_{\text{Shock Externo}} + \eta_t$$

*   **Pilar I:** Fricción Energética.
*   **Pilar II:** Exacción Inmobiliaria.
*   **Pilar III:** Inercia Burocrática.
*   **Pilar IV:** Shocks Externos.

## 4. Arquitectura de Simulación
Simulaciones de Monte Carlo calibradas con datos históricos chilenos.

## 5. Contribución y Licencia
Open Source bajo [MIT License](LICENSE).
