# El Nudo Gordiano: Live Executable Paper

> [!CAUTION]
> ### ⚠️ ALERTA DE SISTEMA: ENTROPÍA ECONÓMICA DETECTADA
> **Este documento es la autopsia en tiempo real del poder adquisitivo bajo fricción fiscal en Chile.**
> *Actualización automatizada de vectores vía mindicador.cl.*

## 📄 Abstract Científico
Este repositorio formaliza un modelo estocástico de fricción fiscal aplicado a la economía chilena. Mediante simulaciones de Monte Carlo, cuantifica la erosión del ingreso real frente a vectores de ineficiencia estructural, tales como el sobreprecio en infraestructura pública y la exacción energética.

## 🔬 Metodología
El modelo opera sobre la hipótesis de que la formación de capital está inversamente correlacionada con la opacidad del gasto estatal. Se integran datos en vivo para recalibrar los intervalos de confianza de la pérdida de valor nominal.

## 🛠️ Infraestructura (Live Engine)
- **Motor de Ingesta**: `src/fetch_data.py` - Captura semanal de UF, UTM e IPC.
- **Simulador Dinámico**: `src/simulador.py` - Incluye lógica de **Cisnes Negros** con diagnósticos de origen causal.
- **Interfaz**: Dashboard brutalista en `index.html` con renderizado de ecuaciones LaTeX.

## ⚙️ Reproducibilidad
```bash
git clone https://github.com/blackmetalhans/nudo-gordiano-economia-cl.git
cd nudo-gordiano-economia-cl
pip install -r requirements.txt
python src/fetch_data.py
python src/simulador.py
```
