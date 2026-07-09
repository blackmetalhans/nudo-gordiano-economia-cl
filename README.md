# El Nudo Gordiano: Anatomía del Derroche Fiscal en Chile

Este repositorio presenta un **paper aplicado** y una base de simulación orientada a medir cómo distintas fricciones del aparato público terminan afectando el ingreso real de la ciudadanía.

La hipótesis central es simple: cuando aumentan los sobrecostos, la ineficiencia administrativa y la exposición a shocks externos, el sistema traslada ese costo al bolsillo del ciudadano mediante precios más altos, menor productividad fiscal y menor capacidad de compra.

## Resumen Ejecutivo

El modelo integra cuatro mecanismos estructurales:

1. **Fraude del Hormigón**: sobreprecio en obras públicas municipales.
2. **Exacción Energética**: sensibilidad del precio final a Brent e impuestos específicos.
3. **Hipertrofia Burocrática**: pérdida de eficiencia por capas administrativas.
4. **Commoditización**: vulnerabilidad a variables externas de mercado.

Con estos componentes, se simulan escenarios para estimar su impacto agregado sobre el indicador:

- **Ingreso Neto Real del Ciudadano**.

## Pregunta de Investigación

> ¿En qué magnitud las distorsiones fiscales y administrativas reducen el ingreso neto real en Chile, y qué variables explican mayor proporción de esa pérdida?

## Estructura del Modelo

Variables incluidas en la simulación base (`data/simulacion_base.csv`):

- `Precio_Brent`
- `Precio_Surtidor_Litro`
- `Costo_M2_Obra_Muni`
- `Eficiencia_Aparato_Estatal`
- `Ingreso_Neto_Real_Ciudadano`

### Lectura conceptual

- **Canal energético**: Brent e impuestos elevan el costo de transporte y cadena logística.
- **Canal de inversión pública**: sobrecostos de obra disminuyen eficiencia del gasto.
- **Canal institucional**: menor eficiencia administrativa amplifica pérdidas de bienestar.

## Resultados Base (lectura cualitativa)

La simulación muestra una dinámica consistente con la hipótesis: cambios aparentemente acotados en variables de costo y eficiencia generan presión sistemática sobre el ingreso real ciudadano. En términos prácticos, la combinación de sobreprecio + fricción institucional tiene efectos persistentes, incluso con variaciones moderadas del entorno externo.

## Implicancias de Política Pública

1. **Auditoría preventiva y trazabilidad de contratos públicos** para reducir sobreprecio.
2. **Rediseño de capas administrativas** con métricas de productividad por unidad fiscal.
3. **Mecanismos de amortiguación energética** para contener traspasos regresivos al consumo.
4. **Gestión de riesgo macro-fiscal** con monitoreo temprano de shocks de commodities.

## Ejecución y Revisión Visual

- El repositorio incorpora una portada visual en `index.html` con narrativa ejecutiva y visualización rápida del estudio.
- Para abrirla localmente, basta con abrir el archivo en navegador o servir el directorio con un servidor estático.

Ejemplo:

```bash
python3 -m http.server 8000
```

Luego visitar `http://localhost:8000/`.

## Estructura del Repositorio

- `README.md`: paper y marco conceptual.
- `index.html`: versión visual/estética del trabajo.
- `data/simulacion_base.csv`: datos de simulación base (regenerado automáticamente).
- `src/simulador.py`: motor de simulación estocástica con parámetros ajustables.
- `requirements.txt`: dependencias Python del simulador.
- `.github/workflows/update_data.yml`: workflow de actualización automática (cron semanal + push).

## Motor de Simulación (`src/simulador.py`)

El simulador regenera `data/simulacion_base.csv` a partir de los cuatro pilares del modelo, aceptando argumentos por línea de comandos para explorar escenarios alternativos.

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
| `--impuesto-especifico` | 2 – Exacción Energética | Impuesto adicional CLP/litro | `0` |
| `--capas-burocraticas` | 3 – Hipertrofia Burocrática | N.° de capas administrativas | `5` |
| `--sobreprecio-construccion` | 1 – Fraude del Hormigón | Sobreprecio % en obras | `0` |
| `--brent-base` | 4 – Commoditización | Precio medio Brent (USD/barril) | `75` |
| `--n` | — | Número de observaciones | `1000` |
| `--seed` | — | Semilla aleatoria | `42` |
| `--output` | — | Ruta CSV de salida | `data/simulacion_base.csv` |

## Actualización Automática (GitHub Actions)

El workflow `.github/workflows/update_data.yml` ejecuta el simulador y hace auto-commit del CSV actualizado:

- **Cron semanal**: todos los lunes a las 06:00 UTC.
- **Con cada push** a la rama `main`.
- **Ejecución manual** desde la pestaña *Actions*, con inputs opcionales para alterar los cuatro pilares en tiempo real.

## Próximos Pasos

- Añadir escenarios contrafactuales con sensibilidad paramétrica.
- Incorporar tests de consistencia estadística del motor de simulación.
- Publicar series comparativas y trazabilidad metodológica completa.
