# El Nudo Gordiano: Live Executable Paper

> **ADVERTENCIA:** Este repositorio opera como un organismo dinámico. Los datos de simulación se recalibran en tiempo real mediante un pipeline automatizado conectado a indicadores financieros chilenos.

## 🔬 Propósito
Formalizar mediante simulación estocástica la **fricción fiscal** en la economía chilena. El modelo analiza cómo vectores de ineficiencia burocrática y exacción energética corroen la formación de capital real.

## 🛠️ Arquitectura Técnica
- **Motor de Ingesta:** `src/fetch_data.py` - Captura automatizada de UF, UTM e IPC.
- **Núcleo Matemático:** `src/simulador.py` - Modelado de Monte Carlo con lógica de cisne negro.
- **Visualización:** Interface basada en HTML5/CSS3 Brutalista con inyección de datos dinámicos.

## 🚀 Reproducibilidad
Para ejecutar la autopsia económica localmente:
```bash
pip install -r requirements.txt
python src/fetch_data.py
python src/simulador.py
```
