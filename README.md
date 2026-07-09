# El Nudo Gordiano: Anatomía del Derroche Fiscal en Chile

[![Reproducibility: Executable Paper](https://img.shields.io/badge/Reproducibility-Executable_Paper-0052cc)](#-reproducibilidad-computacional)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📄 Abstract
Este repositorio formaliza un modelo estocástico de fricción fiscal aplicado a la economía chilena, estructurado como un *Executable Paper*. Mediante simulaciones de Monte Carlo, cuantifica la erosión del ingreso neto real a través de cuatro vectores ortogonales: hipertrofia de gobernanza ($k$-capas), varianza en costos de infraestructura pública, exacción tributaria energética y shocks exógenos de *commodities* (Brent). La arquitectura permite auditoría matemática directa y reproducibilidad determinista de la inferencia.


**Tipo:** Paper Aplicado · Simulación Estocástica · Economía Pública  
**Formato:** Executable Paper (código + datos + visualización reproducible)  
**Repositorio:** `blackmetalhans/nudo-gordiano-economia-cl`

---

## Clasificación JEL

| Código | Área temática |
|--------|---------------|
| **H57** | Procurement · Contratos y Licitaciones Públicas |
| **H72** | Finanzas Subnacionales · Eficiencia del Gasto Municipal |
| **O13** | Recursos Naturales y Energía en el Desarrollo |
| **Q02** | Commodities · Mercados de Materias Primas |
| **D73** | Corrupción · Captura Regulatoria |

---

## Resumen / Abstract

Este trabajo presenta un modelo de simulación estocástica de cuatro pilares para cuantificar cómo fricciones sistémicas del sector público chileno erosionan el ingreso neto real del ciudadano. La hipótesis central es que sobrecostos contractuales, impuestos regresivos sobre la energía, hipertrofia burocrática y volatilidad de commodities actúan de forma sinérgica y persistente sobre el bienestar.  

Se calibraron ecuaciones analíticas sobre parámetros estructurales de la economía chilena y se implementó un motor de simulación Monte Carlo reproducible con interfaz de parámetros ajustables. Los resultados muestran que la combinación de sobreprecio + fricción institucional genera pérdidas persistentes de ingreso incluso bajo variaciones moderadas del entorno externo.

**Palabras clave:** Economía pública, sobrecostos fiscales, exacción energética, ineficiencia burocrática, simulación estocástica, Chile.

---

## Pregunta de Investigación

> ¿En qué magnitud las distorsiones fiscales y administrativas reducen el ingreso neto real en Chile, y qué variables explican mayor proporción de esa pérdida?

---

## Metodología y Formalización Matemática

El modelo integra cuatro pilares de fricción fiscal, cada uno formalizado como un proceso estocástico o función determinística calibrada. La variable de salida unificadora es el **Ingreso Neto Real del Ciudadano** ($I_{neto}$):

$$
I_{neto,t} = Y_0 \cdot \mathcal{E}(k) \;-\; \delta_E \cdot P_{surtidor,t} \;-\; \delta_C \cdot C_{m^2,t}
$$

donde $Y_0 = 1{,}182{,}000$ CLP es el ingreso potencial bruto mensual, $\delta_E = 0.12$ es la fracción del ingreso afectada por el canal energético, y $\delta_C = 0.01$ es la fracción afectada por el canal de obra pública.

---

### Pilar I — Fraude del Hormigón

**Variable modelada:** Costo por m² en obras públicas municipales con sobrecosto fraudulento.

Sea $s$ el porcentaje de sobreprecio y $\mu_{m^2}$ el costo base por m² (CLP). El costo efectivo de obra sigue un proceso estocástico normal con media inflada:

$$
\mu_{m^2}^{eff} = \mu_{m^2} \cdot \left(1 + \frac{s}{100}\right)
$$

$$
C_{m^2} \sim \mathcal{N}\!\left(\mu_{m^2}^{eff},\; \sigma_{m^2}^2\right), \quad C_{m^2} \geq 15{,}000 \text{ CLP/m}^2
$$

**Parámetros de calibración:** $\mu_{m^2} = 30{,}000$ CLP/m², $\sigma_{m^2} = 3{,}000$ CLP/m².

La varianza inducida por el fraude sobre el ingreso neto es:

$$
\text{Var}\!\left[\delta_C \cdot C_{m^2}\right] = \delta_C^2 \cdot \sigma_{m^2}^2 = (0.01)^2 \cdot (3{,}000)^2 = 900 \text{ CLP}^2
$$

El impacto esperado del sobreprecio sobre el ingreso es:

$$
\Delta I_{fraude} = -\delta_C \cdot \mu_{m^2} \cdot \frac{s}{100} = -300 \cdot \frac{s}{100} \text{ CLP/mes}
$$

Con $s = 20\%$, la pérdida esperada alcanza $-60$ CLP/mes por ciudadano de forma directa, con efectos de segunda vuelta sobre la calidad de la infraestructura pública.

---

### Pilar II — Exacción Energética

**Variable modelada:** Precio al surtidor (CLP/litro) en función del Brent y del impuesto específico.

La ecuación de regresión lineal calibrada sobre datos históricos es:

$$
P_{surtidor,t} = \alpha \cdot B_t + \beta + \tau + \varepsilon_t
$$

$$
P_{surtidor,t} = 8.4486 \cdot B_t + 550.93 + \tau + \varepsilon_t, \quad \varepsilon_t \sim \mathcal{N}(0,\; 15^2)
$$

donde:
- $B_t$ = precio spot del Brent en USD/barril en el período $t$
- $\alpha = 8.4486$ CLP/litro por USD/barril (coeficiente de traspaso)
- $\beta = 550.93$ CLP/litro (intercepto: costos de distribución y márgenes de refinación)
- $\tau$ = impuesto específico **adicional** al escenario base (CLP/litro); parámetro del simulador con default `0`. El impuesto base chileno vigente ($\tau_0$) ya opera en la economía real: equivale a ≈6 UTM/m³ (referencia: UTM agosto 2024 = $65,927 CLP → $\tau_0 \approx 222$ CLP/litro); el simulador permite modelar variaciones $\Delta\tau$ sobre dicho nivel
- $\varepsilon_t$ = ruido estocástico de mercado (volatilidad de margen)

El impacto sobre el ingreso neto es:

$$
\frac{\partial I_{neto}}{\partial B_t} = -\delta_E \cdot \alpha = -0.12 \times 8.4486 \approx -1.014 \text{ CLP/mes por USD/barril de Brent}
$$

Ante un shock de $\Delta B = +10$ USD/barril, el ingreso neto cae en promedio ≈10.14 CLP/mes por vía del canal energético directo.

---

### Pilar III — Hipertrofia Burocrática

**Variable modelada:** Eficiencia del aparato estatal en función del número de capas administrativas.

Sea $k$ el número de capas de gobernanza. La función de eficiencia es lineal por tramos con piso de subsistencia:

$$
\mathcal{E}(k) = \max\!\left(0.05,\; 1 - 0.09 \cdot k\right)
$$

El ingreso bruto efectivo aplicable al ciudadano es:

$$
Y_{bruto}(k) = Y_0 \cdot \mathcal{E}(k) = 1{,}182{,}000 \cdot \mathcal{E}(k) \text{ CLP/mes}
$$

**Calibración sobre estructura institucional chilena:** Con las 4 capas de gobernanza características (GORE, Delegados Presidenciales, SEREMI y Municipio), más la capa de coordinación central ($k = 5$):

$$
\mathcal{E}(5) = 1 - 0.09 \times 5 = 0.55
$$

La pérdida de eficiencia respecto al óptimo sin fricción ($k=0$, $\mathcal{E}=1$) es del 45%, equivalente a una contracción del ingreso potencial de:

$$
\Delta Y_{burocracia} = Y_0 \cdot [1 - \mathcal{E}(k)] = 1{,}182{,}000 \cdot 0.45 = 531{,}900 \text{ CLP/mes}
$$

Cada capa adicional tiene un costo marginal de:

$$
\frac{\partial Y_{bruto}}{\partial k} = -Y_0 \times 0.09 = -106{,}380 \text{ CLP/mes por capa}
$$

---

### Pilar IV — Commoditización

**Variable modelada:** Función de transferencia que acopla la volatilidad del Brent al Ingreso Neto Real.

El precio del Brent sigue un proceso estocástico normal con truncamiento inferior:

$$
B_t \sim \mathcal{N}\!\left(\mu_B,\; \sigma_B^2\right), \quad B_t \geq 20 \text{ USD/barril}
$$

**Parámetros base:** $\mu_B = 75$ USD/barril, $\sigma_B = 12$ USD/barril.

La función de transferencia completa que acopla el Brent al Ingreso Neto es, sustituyendo el Pilar II en la ecuación maestra:

$$
I_{neto,t} = \underbrace{Y_0 \cdot \mathcal{E}(k)}_{\text{Pilar III}} - \underbrace{\delta_E \cdot (\alpha \cdot B_t + \beta + \tau + \varepsilon_t)}_{\text{Pilar II}} - \underbrace{\delta_C \cdot C_{m^2,t}}_{\text{Pilar I}}
$$

Expandiendo y agrupando términos determinísticos y estocásticos:

$$
I_{neto,t} = \underbrace{\left[Y_0 \cdot \mathcal{E}(k) - \delta_E(\beta + \tau) - \delta_C \cdot \mu_{m^2}^{eff}\right]}_{\mu_{I}} - \underbrace{\delta_E \cdot \alpha}_{\phi} \cdot B_t + \eta_t
$$

donde $\phi = \delta_E \cdot \alpha = 0.12 \times 8.4486 \approx 1.014$ es el **coeficiente de transmisión del Brent al ingreso** (CLP/mes por USD/barril), y el término de ruido agregado es:

$$
\eta_t = -\delta_E \cdot \varepsilon_t - \delta_C \cdot \xi_t \sim \mathcal{N}\!\left(0,\; \delta_E^2 \sigma_\varepsilon^2 + \delta_C^2 \sigma_{m^2}^2\right)
$$

$$
\text{Var}[\eta_t] = (0.12)^2 \cdot (15)^2 + (0.01)^2 \cdot (3{,}000)^2 = 3.24 + 900 = 903.24 \text{ CLP}^2
$$

Los límites de control estadístico $\mu_I \pm 3\sigma_I$ (bandas $3\sigma$) de la serie de ingreso neto engloban la dispersión simulada en el gráfico de la interfaz web.

---

## Estructura del Repositorio

```
nudo-gordiano-economia-cl/
├── README.md                          # Este paper
├── index.html                         # Executable Paper: landing visual interactiva
├── data/
│   └── simulacion_base.csv            # Dataset regenerado automáticamente por CI/CD
├── src/
│   └── simulador.py                   # Motor de simulación Monte Carlo
├── requirements.txt                   # Dependencias Python
└── .github/
    └── workflows/
        └── update_data.yml            # Pipeline de datos automatizado (CI/CD)
```

### Variables del dataset (`data/simulacion_base.csv`)

| Variable | Unidad | Descripción |
|---|---|---|
| `Precio_Brent` | USD/barril | Precio spot simulado del crudo Brent |
| `Precio_Surtidor_Litro` | CLP/litro | Precio final al surtidor (Pilar II) |
| `Costo_M2_Obra_Muni` | CLP/m² | Costo de obra municipal con sobreprecio (Pilar I) |
| `Eficiencia_Aparato_Estatal` | adimensional [0,1] | Eficiencia resultante de las capas de gobernanza (Pilar III) |
| `Ingreso_Neto_Real_Ciudadano` | CLP/mes | Ingreso neto real resultante (variable de salida) |

---

## Arquitectura CI/CD: Pipeline de Datos Automatizado

El archivo `.github/workflows/update_data.yml` implementa un **pipeline de datos asíncrono** que garantiza la reproducibilidad y actualización continua del dataset de simulación. A continuación se describe su arquitectura en detalle.

### Diagrama de flujo del pipeline

```
Trigger (cron / push / dispatch)
        │
        ▼
┌───────────────────────┐
│  actions/checkout@v4  │  ← Clona el repositorio en el runner ubuntu-latest
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  setup-python@v5      │  ← Configura Python 3.11 con caché de pip
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  pip install -r       │  ← Instala dependencias (numpy, etc.)
│  requirements.txt     │
└───────────┬───────────┘
            │
        ┌───┴────────────────────────────┐
        │                                │
        ▼                                ▼
┌──────────────────┐          ┌──────────────────────┐
│ Parámetros base  │          │  Parámetros manuales  │
│ (cron / push)    │          │  (workflow_dispatch)  │
│ seed=run_number  │          │  seed=run_number      │
│ n=1000           │          │  n=1000               │
│                  │          │  + inputs del usuario │
└────────┬─────────┘          └──────────┬───────────┘
         └────────────┬──────────────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │   src/simulador.py     │  ← Motor Monte Carlo (Pilares I–IV)
         │   → data/simulacion_   │
         │     base.csv           │
         └────────────┬───────────┘
                      │
                      ▼
         ┌────────────────────────┐
         │ git-auto-commit@v5     │  ← Auto-commit si el CSV cambió
         │ Commit firmado por     │
         │ github-actions[bot]    │
         └────────────────────────┘
```

### Mecanismos de activación

| Trigger | Condición | Semilla |
|---|---|---|
| **`schedule` (cron)** | Todos los lunes 06:00 UTC | `github.run_number` (único por ejecución) |
| **`push` a `main`** | Con cada commit en rama principal | `github.run_number` |
| **`workflow_dispatch`** | Ejecución manual desde pestaña *Actions* | `github.run_number` |

### Parametrización dinámica via `workflow_dispatch`

El pipeline expone cuatro inputs opcionales que mapean directamente a los pilares del modelo, permitiendo explorar escenarios alternativos **sin modificar código**:

| Input | Pilar | Valor por defecto |
|---|---|---|
| `impuesto_especifico` | II – Exacción Energética | `0` CLP/litro |
| `capas_burocraticas` | III – Hipertrofia Burocrática | `5` |
| `sobreprecio_construccion` | I – Fraude del Hormigón | `0` % |
| `brent_base` | IV – Commoditización | `75` USD/barril |

### Reproducibilidad determinística

La semilla `--seed ${{ github.run_number }}` garantiza que cada ejecución del pipeline produce un dataset **único pero reproducible**: dado el mismo `run_number`, el dataset es idéntico. Esta propiedad es fundamental para trazabilidad científica y auditoría de resultados.

---

## Resultados Base

Con los parámetros por defecto ($k=5$, $s=0\%$, $\mu_B=75$ USD/barril, $\tau=0$):

$$
\mathcal{E}(5) = 0.55 \implies Y_{bruto} = 650{,}100 \text{ CLP/mes}
$$

$$
\mathbb{E}[P_{surtidor}] = 8.4486 \times 75 + 550.93 = 1{,}184.58 \text{ CLP/litro}
$$

$$
\mathbb{E}[I_{neto}] = 650{,}100 - 0.12 \times 1{,}184.58 - 0.01 \times 30{,}000 \approx 649{,}658 \text{ CLP/mes}
$$

La simulación es consistente con la hipótesis: la combinación de sobreprecio + fricción institucional genera presión sistemática y persistente sobre el ingreso real.

---

## Implicancias de Política Pública

1. **Auditoría preventiva y trazabilidad de contratos públicos** — reducir $s$ hacia cero elimina la varianza inducida por fraude y recupera $\delta_C \cdot \mu_{m^2} \cdot s/100$ CLP/mes por ciudadano.
2. **Rediseño de capas administrativas** — cada capa eliminada recupera ≈106,380 CLP/mes de ingreso potencial ($\partial Y_{bruto}/\partial k = -106{,}380$).
3. **Mecanismos de amortiguación energética** — subsidios o impuestos negativos que actúen sobre $\tau$ reducen el traspaso del Brent al ingreso con elasticidad $\phi = 1.014$.
4. **Gestión de riesgo macro-fiscal** — cobertura (hedging) sobre el Brent mitiga la volatilidad $\sigma_B$ que se propaga al ingreso neto con coeficiente $\phi$.

---

## Motor de Simulación (`src/simulador.py`)

### Instalación

```bash
pip install -r requirements.txt
```

### Uso

```bash
# Escenario base (parámetros por defecto)
python src/simulador.py

# Subir el Impuesto Específico al combustible (Pilar 2)
python src/simulador.py --impuesto-especifico 150

# Aumentar capas burocráticas (Pilar 3)
python src/simulador.py --capas-burocraticas 8

# Combinar: mayor impuesto + más burocracia + sobreprecio en obras
python src/simulador.py \
  --impuesto-especifico 200 \
  --capas-burocraticas 9 \
  --sobreprecio-construccion 25 \
  --brent-base 95

# Guardar en archivo distinto (sin sobreescribir el CSV base)
python src/simulador.py --capas-burocraticas 10 --output /tmp/escenario_extremo.csv

# Ver todas las opciones
python src/simulador.py --help
```

### Parámetros principales

| Argumento | Pilar | Descripción | Default |
|---|---|---|---|
| `--impuesto-especifico` | II – Exacción Energética | Incremento adicional Δτ sobre el impuesto base (CLP/litro). El impuesto base real (~222 CLP/litro) opera fuera del simulador. | `0` |
| `--capas-burocraticas` | III – Hipertrofia Burocrática | N.° de capas administrativas | `5` |
| `--sobreprecio-construccion` | I – Fraude del Hormigón | Sobreprecio % en obras | `0` |
| `--brent-base` | IV – Commoditización | Precio medio Brent (USD/barril) | `75` |
| `--n` | — | Número de observaciones | `1000` |
| `--seed` | — | Semilla aleatoria | `42` |
| `--output` | — | Ruta CSV de salida | `data/simulacion_base.csv` |

### Ejecución visual (interfaz web)

El repositorio incorpora una portada visual en `index.html` con narrativa ejecutiva, KPIs en tiempo real y un modal de formulación científica interactivo.

```bash
python3 -m http.server 8000
# Visitar http://localhost:8000/
```

---

## Próximos Pasos

- Añadir escenarios contrafactuales con análisis de sensibilidad paramétrica ($\partial I_{neto}/\partial \theta_i$).
- Incorporar tests de consistencia estadística (Kolmogorov-Smirnov, test de normalidad) del motor de simulación.
- Publicar series comparativas con datos reales del INE/CNE para validación empírica del modelo.
- Estimar intervalos de confianza bootstrap para los coeficientes calibrados ($\alpha$, $\delta_E$, $\delta_C$).

---
## ⚙️ Reproducibilidad Computacional

Para auditar o recalibrar la inferencia estocástica localmente, el modelo requiere Python 3.10+ y la regeneración de la semilla de Monte Carlo.

```bash
# 1. Clonar repositorio y levantar entorno aisaldo
git clone https://github.com/blackmetalhans/nudo-gordiano-economia-cl.git
cd nudo-gordiano-economia-cl
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

# 2. Instalar dependencias del motor matemático
pip install numpy pandas scipy

# 3. Ejecutar simulación base (sobrescribe data/simulacion_base.csv)
python src/simulador.py --iterations 10000 --seed 42
```
