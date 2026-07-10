# El Nudo Gordiano de la Economía Chilena

[![Executable Paper](https://img.shields.io/badge/Paper-Executable-blue.svg)](https://blackmetalhans.github.io/nudo-gordiano-economia-cl/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Executable Paper:** Modelado estocástico de ineficiencias estructurales y pérdida de bienestar agregado en Chile.

**Autor:** Hans Soriano | **Estado:** Producción (v3.0.0-integral)

---

## 📋 Índice de Navegación

- [Executive Summary](#executive-summary)
- [Ecuación Fundamental de Bienestar](#ecuación-fundamental-de-bienestar)
- [Marco Teórico: Los Cuatro Pilares](#marco-teórico-los-cuatro-pilares)
- [Arquitectura CI/CD y Pipeline de Datos](#arquitectura-cicd-pipeline-de-datos-automatizado)
- [Reproducibilidad Local](#reproducibilidad-local)
- [Estructura del Repositorio](#estructura-del-repositorio)
- [Motor de Simulación](#motor-de-simulación)
- [Implicancias de Política Pública](#implicancias-de-política-pública)
- [Próximos Pasos](#próximos-pasos)

---

## Executive Summary

Este repositorio cuantifica matemáticamente la **histéresis del desarrollo en Chile**, modelando el colapso de la Productividad Total de Factores (PTF) desde la perspectiva del ingreso neto ciudadano.

El modelo abandona el análisis discursivo tradicional para plantear un sistema de ecuaciones estocásticas **calibrables y auditables en tiempo real**. La ingesta de datos está automatizada mediante GitHub Actions, garantizando reproducibilidad continua.

**Clasificación JEL:**
- **H57**: Procurement · Contratos y Licitaciones Públicas
- **H72**: Finanzas Subnacionales · Eficiencia del Gasto Municipal
- **O13**: Recursos Naturales y Energía en el Desarrollo
- **Q02**: Commodities · Mercados de Materias Primas
- **D73**: Corrupción · Captura Regulatoria

---

## Ecuación Fundamental de Bienestar

$$I_{neto,t} = \underbrace{Y_0 \cdot \mathcal{E}(k)}_{\text{Rendimiento Base}} - \underbrace{\delta_E(\beta+\tau)}_{\text{Fricción Energética}} - \underbrace{\delta_C\mu_{m^2}^{eff}}_{\text{Exacción Inmob.}} - \underbrace{\phi B_t}_{\text{Shock Externo}} + \eta_t$$

donde:
- $Y_0 = 1{,}182{,}000$ CLP es el ingreso potencial bruto mensual
- $\mathcal{E}(k)$ es la eficiencia del aparato estatal en función de capas administrativas
- $\delta_E$ y $\delta_C$ son fracciones del ingreso afectadas por fricción energética e inmobiliaria
- $\eta_t$ es ruido blanco amplificado por fallas de mercado

---

## Marco Teórico: Los Cuatro Pilares

### Pilar I — Fraude del Hormigón

**Variable modelada:** Costo por m² en obras públicas municipales con sobrecosto fraudulento.

$$\mu_{m^2}^{eff} = \mu_{m^2} \cdot \left(1 + \frac{s}{100}\right)$$

$$C_{m^2} \sim \mathcal{N}\!\left(\mu_{m^2}^{eff},\; \sigma_{m^2}^2\right), \quad C_{m^2} \geq 15{,}000 \text{ CLP/m}^2$$

**Parámetros:** $\mu_{m^2} = 30{,}000$ CLP/m², $\sigma_{m^2} = 3{,}000$ CLP/m².

Con $s = 20\%$, la pérdida esperada alcanza $\Delta I_{fraude} = -60$ CLP/mes por ciudadano.

---

### Pilar II — Exacción Energética

**Variable modelada:** Precio al surtidor (CLP/litro) en función del Brent y del impuesto específico.

$$P_{surtidor,t} = 8.4486 \cdot B_t + 550.93 + \tau + \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0,\; 15^2)$$

donde:
- $B_t$ = precio spot del Brent (USD/barril)
- $\tau$ = impuesto específico adicional (CLP/litro)
- $\alpha = 8.4486$ es el coeficiente de traspaso

Ante un shock de $\Delta B = +10$ USD/barril, el ingreso neto cae ≈10.14 CLP/mes.

---

### Pilar III — Hipertrofia Burocrática

**Variable modelada:** Eficiencia estatal en función del número de capas administrativas.

$$\mathcal{E}(k) = \max\!\left(0.05,\; 1 - 0.09 \cdot k\right)$$

Con las 5 capas típicas de gobernanza chilena: $\mathcal{E}(5) = 0.55$

La pérdida de eficiencia representa una contracción del ingreso potencial de:

$$\Delta Y_{burocracia} = Y_0 \cdot [1 - \mathcal{E}(k)] = 531{,}900 \text{ CLP/mes}$$

Cada capa adicional cuesta ≈106,380 CLP/mes de ingreso potencial.

---

### Pilar IV — Commoditización

**Variable modelada:** Función de transferencia que acopla la volatilidad del Brent al ingreso neto real.

$$B_t \sim \mathcal{N}\!\left(75,\; 12^2\right), \quad B_t \geq 20 \text{ USD/barril}$$

El coeficiente de transmisión es $\phi = \delta_E \cdot \alpha \approx 1.014$ CLP/mes por USD/barril.

---

## Arquitectura CI/CD: Pipeline de Datos Automatizado

El pipeline está implementado en `.github/workflows/update_data.yml` y garantiza reproducibilidad mediante:

### Mecanismos de Activación

| Trigger | Condición | Semilla |
|---|---|---|
| **schedule** (cron) | Todos los lunes 06:00 UTC | `github.run_number` |
| **push** a `main` | Con cada commit | `github.run_number` |
| **workflow_dispatch** | Ejecución manual | `github.run_number` |

### Flujo del Pipeline

```
Trigger (cron / push / dispatch)
         │
         ▼
    Checkout + Setup Python
         │
    ┌────┴───────┬────────────────────┐
    │            │                    │
   Cron        Push           workflow_dispatch
    │            │                    │
    └────┬───────┴────────────────────┘
         │
         ▼
    src/simulador.py
         │
    ▼   (ejecuta Monte Carlo)
    data/simulacion_base.csv
         │
         ▼
    auto-commit (si cambió)
```

### Parametrización Dinámica

El workflow expone inputs opcionales para explorar escenarios alternativos sin modificar código:

| Input | Pilar | Default |
|---|---|---|
| `impuesto_especifico` | II – Exacción Energética | `0` CLP/litro |
| `capas_burocraticas` | III – Hipertrofia Burocrática | `5` |
| `sobreprecio_construccion` | I – Fraude del Hormigón | `0` % |
| `brent_base` | IV – Commoditización | `75` USD/barril |

---

## Reproducibilidad Local

### 1. Clonar el Repositorio

```bash
git clone https://github.com/blackmetalhans/nudo-gordiano-economia-cl.git
cd nudo-gordiano-economia-cl
```

### 2. Instalar Dependencias

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Simulación

```bash
# Con parámetros por defecto
python src/simulador.py

# Con parámetros personalizados
python src/simulador.py \
  --impuesto-especifico 200 \
  --capas-burocraticas 9 \
  --sobreprecio-construccion 25 \
  --brent-base 95

# Ver todas las opciones
python src/simulador.py --help
```

### 4. Ejecutar con Servidor Web (Interfaz Interactiva)

```bash
python3 -m http.server 8000
# Acceder a http://localhost:8000
```

---

## Estructura del Repositorio

```
nudo-gordiano-economia-cl/
├── README.md                          # Este documento
├── index.html                         # Landing visual interactiva (Executable Paper)
├── data/
│   └── simulacion_base.csv            # Dataset regenerado automáticamente
├── src/
│   ├── simulador.py                   # Motor de simulación Monte Carlo
│   └── fetch_data.py                  # Ingesta de indicadores macroeconómicos
├── requirements.txt                   # Dependencias Python
└── .github/
    └── workflows/
        └── update_data.yml            # Pipeline CI/CD automatizado
```

### Dataset: Variables de Salida

| Variable | Unidad | Descripción |
|---|---|---|
| `Precio_Brent` | USD/barril | Precio spot simulado del crudo |
| `Precio_Surtidor_Litro` | CLP/litro | Precio final al surtidor (Pilar II) |
| `Costo_M2_Obra_Muni` | CLP/m² | Costo de obra municipal (Pilar I) |
| `Eficiencia_Aparato_Estatal` | [0,1] | Eficiencia estatal (Pilar III) |
| `Ingreso_Neto_Real_Ciudadano` | CLP/mes | Ingreso neto resultado |

---

## Motor de Simulación

### Parámetros Principales

| Argumento | Pilar | Descripción | Default |
|---|---|---|---|
| `--impuesto-especifico` | II | Incremento Δτ sobre impuesto base | `0` |
| `--capas-burocraticas` | III | Número de capas administrativas | `5` |
| `--sobreprecio-construccion` | I | Sobreprecio % en obras | `0` |
| `--brent-base` | IV | Precio medio Brent | `75` |
| `--n` | — | Observaciones | `1000` |
| `--seed` | — | Semilla aleatoria | `42` |
| `--output` | — | Ruta CSV de salida | `data/simulacion_base.csv` |

---

## Resultados Base

Con parámetros por defecto ($k=5$, $s=0\%$, $\mu_B=75$ USD/barril, $\tau=0$):

$$\mathcal{E}(5) = 0.55 \implies Y_{bruto} = 650{,}100 \text{ CLP/mes}$$

$$\mathbb{E}[P_{surtidor}] = 8.4486 \times 75 + 550.93 = 1{,}184.58 \text{ CLP/litro}$$

$$\mathbb{E}[I_{neto}] \approx 649{,}658 \text{ CLP/mes}$$

La simulación es consistente: la combinación de sobreprecio + fricción institucional genera presión sistemática sobre el ingreso real.

---

## Implicancias de Política Pública

1. **Auditoría preventiva de contratos públicos** — reducir $s$ hacia cero elimina la varianza inducida por fraude y recupera $\delta_C \cdot \mu_{m^2} \cdot s/100$ CLP/mes por ciudadano.

2. **Rediseño de capas administrativas** — cada capa eliminada recupera ≈106,380 CLP/mes de ingreso potencial.

3. **Mecanismos de amortiguación energética** — subsidios o impuestos negativos sobre $\tau$ reducen el traspaso del Brent con elasticidad $\phi = 1.014$.

4. **Gestión de riesgo macro-fiscal** — cobertura sobre el Brent mitiga la volatilidad que se propaga al ingreso neto.

---

## Próximos Pasos

- [ ] Añadir escenarios contrafactuales con análisis de sensibilidad paramétrica
- [ ] Incorporar tests de consistencia estadística (Kolmogorov-Smirnov, normalidad)
- [ ] Publicar series comparativas con datos reales (INE/CNE) para validación empírica
- [ ] Estimar intervalos de confianza bootstrap para coeficientes calibrados
- [ ] Expandir a análisis de regímenes (Markov-switching) para captar ciclos económicos

---

## Licencia

**MIT License** — Libre para uso comercial, modificación y distribución con atribución.

## Disclaimer Académico

La formulación metodológica expuesta representa un **modelo simplificado estocástico** de fallas estructurales. Modificaciones de shocks extremos requieren recalibración según contexto macroeconómico.

---

**Última actualización:** 2026-07-10 | **Datos actualizados:** Automático (semanalmente los lunes)
