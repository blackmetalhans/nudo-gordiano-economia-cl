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
- `data/simulacion_base.csv`: datos de simulación base.

## Próximos Pasos

- Añadir escenarios contrafactuales con sensibilidad paramétrica.
- Incorporar tests de consistencia estadística del motor de simulación.
- Publicar series comparativas y trazabilidad metodológica completa.
