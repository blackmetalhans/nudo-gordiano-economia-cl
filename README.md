# **El Nudo Gordiano de la Economía Chilena**

[![Executable Paper](https://img.shields.io/badge/Paper-Executable-blue.svg)](https://blackmetalhans.github.io/nudo-gordiano-economia-cl/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Modelado Estocástico de Ineficiencias Estructurales y Pérdida de Bienestar Agregado**

Este repositorio constituye un **Executable Paper**. Cuantifica la histéresis del desarrollo en Chile mediante un sistema de ecuaciones estocásticas calibrables.

## **Ecuación Fundamental de Bienestar**

$$I_{neto,t} = \underbrace{Y_0 \cdot \mathcal{E}(k)}_{\text{Rendimiento Base}} - \underbrace{\delta_E(\beta+\tau)}_{\text{Fricción Energética}} - \underbrace{\delta_C\mu_{m^2}^{eff}}_{\text{Exacción Inmob.}} - \underbrace{\phi B_t}_{\text{Shock Externo}} + \eta_t$$

---
## **Índice de Navegación**
* [Ecuación Fundamental de Bienestar](#ecuación-fundamental-de-bienestar)
* [1\. Marco Teórico y Formulación Estocástica](#1\-marco-teórico-y-formulación-estocástica)
  * [ºLos Cuatro Pilares del Estancamiento](#ºlos-cuatro-pilares-del-estancamiento)
* [2\. Arquitectura de Datos (CI/CD Pipeline)](#2\-arquitectura-de-datos-ci/cd-pipeline)
* [3\. Reproducibilidad Local](#3\-reproducibilidad-local)

---

# **El Nudo Gordiano de la Economía Chilena**


*Autor: Hans Soriano | Estado: Producción (v3.0.0-integral)*

Este repositorio constituye un **Executable Paper**. Su objetivo es cuantificar matemáticamente la histéresis del desarrollo en Chile, modelando el colapso de la Productividad Total de Factores (PTF) desde la perspectiva del ingreso neto ciudadano (). El modelo abandona el análisis discursivo tradicional para plantear un sistema de ecuaciones estocásticas calibrables y auditables en tiempo real.

## **1\. Marco Teórico y Formulación Estocástica**

El sistema asume que el ingreso ciudadano está sujeto a un vector de fricciones institucionales y de mercado. La ecuación fundamental de transferencia de bienestar define la esperanza matemática del ingreso en el periodo  como:

Donde la varianza del sistema (ruido blanco amplificado por fallas de mercado) está dada por:

### **ºLos Cuatro Pilares del Estancamiento**

1. **Hipertrofia Burocrática ():** El costo de agencia estatal se modela como una función de decrecimiento . La línea base chilena () destruye masivamente el rendimiento productivo óptimo antes de que el capital fluya hacia la economía real.  
2. **Exacción Inmobiliaria ():** La desviación especulativa del suelo se modela como . Este sobreprecio drena liquidez del sector productivo hacia la acumulación pasiva de capital rentista.  
3. **Indexación Asimétrica Energética ():** El impuesto específico opera como una cuña fiscal profundamente regresiva que encarece de manera transversal toda la matriz logística nacional.  
4. **Commoditización (Brent ):** Proceso estocástico del valor del crudo acoplado directamente al consumo interno, exponiendo la falta de complejidad económica local.

## **2\. Arquitectura de Datos (CI/CD Pipeline)**

Para garantizar que el ensayo sea verdaderamente reproducible y mantener el documento "vivo", la ingesta de datos está automatizada mediante **GitHub Actions**.

* **.github/workflows/update\_data.yml:** Tarea que ejecuta la ingesta de indicadores.  
* **src/fetch\_data.py:** Extrae la UF, UTM y Dólar actualizados vía API y reconstruye el vector inicial en data/live\_data.json.  
* **src/simulador.py:** Motor en Python que lee la topología de la red, inyecta las variables macroeconómicas actualizadas, ejecuta la inferencia de Montecarlo y arroja el volcado a data/simulacion\_base.csv.

## **3\. Reproducibilidad Local**

Si deseas correr el motor de inferencia analítico en tu entorno local:

\# 1\. Clonar el repositorio  
git clone https://github.com/blackmetalhans/nudo-gordiano-economia-cl.git  
cd nudo-gordiano-economia-cl

\# 2\. Instalar dependencias del motor  
pip install \-r requirements.txt

\# 3\. Actualizar la data macroeconómica y simular  
python src/fetch\_data.py  
python src/simulador.py

La inferencia visual (interactiva) se encuentra encapsulada directamente en index.html mediante un motor renderizado en *Canvas*, sin dependencias pesadas.

**Licencia:** MIT.

**Disclaimer Académico:** La formulación metodológica expuesta representa un modelo simplificado estocástico de fallas estructurales. Modificaciones de *shocks* extremos requieren recalibración de la varianza.

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAaCAYAAAAwspV7AAAB3klEQVR4XrVWCXLDMAi0PmL//5VpuA8BcqfTnXEtdheEiOP0uhSLL49vvOBKnLvRcuc8iPaiZvwPpuKTNqPLjAerlg41i7RIxxoNNvNy3CY6lBqR+LfUR8SjPM/zgevmO1738ykrZ4rjTPfwzkOWNGMMJBySFG99DiFFg1joeW6c1NwM8d33CNlaYki+Lo2W2MS1T2osfqF+suCrxYchcgiC646eIY9cIsd8QHfKdy10vIIMOqVwep9cFao4hkpTDb8ZLsLu3NR9eJ4GvEkZPOUgZFLlARVFw+mZiZg0Qu/4KvStk9hvnpvYFtmBiK8WhjNWOQRWtm/dn0BFc72+iQCywd/clBSAZ0z46IlbeE3WuSZiRe/YKBrhdcAubJRfD9WG6kkb0zpOyg5YeRNgUzHSBVOxyUA52dgXFk1irMO1RMo+8WoQPAXaES6bBoehEB2kLky8Vb6xaXjdGPbcthOBTEIK2WSwOffRkk6QGO8wDf2FoJ8w9fnJsj6/WhDcRPrXxU8HPlyJPZ99mdt/yjzGxkbxqvSdaTAbYWR8L3lahvsG9iZ9K3usw5DEky/C3L/Lu6z5NnE7Res0HCxZDjE/xMKtZf8iRp8POhSmguoxmVutFU4oz1nEQhV8gR/Q2YXz11IpJAAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAaCAYAAACKER0bAAAAvElEQVR4Xm1RgQGAIAxyj8z/r7TYxsRypSYgoxrDBm4p7BKxWGI+JaxClfzZZYWHEMYWCl1XbY9TuOac6xTQzkD6mj5Xt/jm8RbUMU6MlPYk6gEgTvnco4VbCfskAy7XzoAVAd29AlqEliCvwKU/OIMoubCHQ+6kL4tBY1PBD1kIELBQhzgiVIj4gtVGv0XqqexwOXaJkkT8NryFyJKg4M/sh5Orvj0I3uxZO881qQQlRP6DSJsDrIk/6h0P6Swn5ULAw9MAAAAASUVORK5CYII=>

[image3]: <data:image/png;base64,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>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAwAAAAZCAYAAAAFbs/PAAAAwklEQVR4Xn1TARLDIAirHyn/f2V3YpBEcLlbhZCApbfn2RhyJA4i06IE1RluWo46Iadd3REFs/d7zT7DL4sHuNM87IWY+BIHsvuodSEwxg2Y0BuGFuY7yB3/Y02ILBewllF68HamiLmrIbpuciz+1DrYcIoyRjQ3s0XeFfcGOHacXSMPs5NRnKfcG+w2hTLGx6m7x5fGo5Q1IarwMSFTVepBSe/a8dWQBe1QDRxp8yQEPLrUm/9GVepaQWUcKHXmEf0AtL05dqqh238AAAAASUVORK5CYII=>

[image5]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQMAAAAaCAYAAACzfzksAAAFNUlEQVR4Xu2cjXLiMAyEy4vQ93/KuzGpQN7synJiJ4H2m8kcXq9+rAAt3M19fXlu1eoPx9TR+OS3ybVO58qnm9DbkJRDkuTQpfTOECanHwNrsmhMf29Gn6jONzI75sL1NsZk+TUkx5W0DSNbL+v743Te61bdTuz3vMqU7+/vf6i12BLz4GJnDxG9Cnm1sXlGvwA5wy0MTbaPLfd8avulIXZ5jzWAumkqzhPtPZl60uPoPcZjNiLoMde7mN0zhgdvuSdM62Fv/Aha545Yx/bN1r9W/FWZHHSPl5zL0khdWTWvdCPaMzKeNp2T6rQvbArahJor6syjyMaaz1/oeRKMJJ0jSVAq5Fn/J0HUC9bA3l+P49dHVKPQ2i9kPFPBQ3kdtYLSCyoXkvPhbfps2DzUnJiG9MSaV8X0MipPAZ8FuEZUbaYVfL5sLPMxzYj2PGtf67SDWTcQcFsPxtOTy3wHH/eysLmpeTIN6YllWkV1k9p3TNXuoV3F83Kr2pWGyd1vEM3YnzVqpqNWUH5GxoftD6O30cgb7SE93ohpg2nQmoWR6U/l6tU9ysN0XO+F1TgKVZvqcHOoh+i49m8mIK30Fj3eNZlnW4AdzF/oMaK9gt8vX3ZFOVFrHaO136LEYz9+rTTTDdRwbdqd5MC19/u1wbyR7lEeppvmL7/fJPmiarH3HhesdpXrlutJeVDHdUb3j/3lfbZfCe4gI+bTRDWGRB6fw/+pcisd8TmyF+ZAmC+liScV05i+8lQ/Uda3uop325iXwT03qrM1aj3sjW+znpXBa/NzI8qDOq69pnR77J9D6EX/IdgoewtH3keun98GUPdro7f2SFjtrMaoffUT1fZoHv9mQJ7fKk7pHuV56qSeoWKz7I2PCNp+oGor3aM8TMe/5jXPyhfo5U88D/O2wSwb6C0a+f2hI5+R9c2A1c5qhu35Cz1GZh+1gopTukd5lI5kPIpsDY/FZK46sv6XgNyjdY/ytHTbYz7vwT1G1pcj+SaxpWjk93uZ3BlPwXzt6/58jDkQ5pPavf78KX1B3cw+agUVV7TynQTqnijW67imevI5ZaicMZ1FBKr2S9d12rExtWep47VMnoynG33khajoFt3v2Zdnr/17/YXOQ+O5jgD77dX82jTmtb3WZ1aml3mxj10Fyxmh6qHGfGXderOJYDmPwmrfYDyZflTfqDGf16w0+tjaHkfadLAxr6Nm0L3bOpdf05gvrR8B9tur+bVpGS/zmL48Wr/A0c9yZOvjm3QB16ahrmowsr5ZYG3Wz/M85LP/8uj1kx3fGFU+vzbN637N/AWlT8Uawwt9nrKPgzGdaUw3or1Z4Fmth4yW1ZlH1Ufd1h6MafmYlo1druXjFnoKUY5CnSeuOROsr3pgexiH+0bWwzSmG9Fei+pHyfrnygA2/LrVojWQU5kyxDaXnQfw7LNjTh3W63LAIc57XWw83IhmeQ7VkNIL0V6ADHMb9lB6x8JncjTtw7b6bGcYB9bC9ZHsr718r4TqfvZ3FrK3afZRo5/XIScfdz4/B0jP9aQDp/tDuvrtMg9nbvU4e3O+cXiKASlqmk0H7IkdcZIBKZLkK5lz12wO4Or97SF/t0azVL7YbPvGsaX5LTHvzHqia6XgVZwRjaBiRHfAG3DSfzs2oSje80KqTMr0TtADoYjr9+P9T7Dm8DO5gtNrTy/g6SzWaf8wfvfpd9Exug7rZfmEM2zl2me/dnchu1qXwXLjrZh6iqnJP5GjBnZUnYgr9PDred2Es27HWXWvzf6p/Ae7NcYIdPXq7gAAAABJRU5ErkJggg==>

[image6]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAaCAYAAAD1wA/qAAACE0lEQVR4XsVXCW7EMAiMP5L8/5VtfWBgGGxH2rYjRTXDcOZY9brKFUCoFyiH8VxVWe5hIEpHiUF0tlHq/kXk9XKP38w4oBztE/AYzlpgL0u45icTjwwbt0FJF6NQzQpOIsbzPF9y3T+X+ntSzIs2Ms2Kog00oPZhHCnXwOo8z03ETBlRVaLMIrafguGWhdZ++oK3ffkttKkntSmKKH6YFVJNS1DMIKOn6XNqQOleF6RO+Cum2svcE9pF1EfG9uG8hakBcvuacKvuMPMMgpEdCU3x3H2QGCJM9EzYLcjdkcuGLVIs8SYH1m+D2Q1nCSRAzpYTO6Jnk0KusLn0WZcXN9u2oL8j/WRqVG53W23hKu1yTUjLHtxliqlfB1qvDqIciU6+Ev8MXWg/9L5I+xa2eTvMJqxB9HixR0ou36VFXWrXd0shOQ2lqMKZfIDZcj4D7XDQ6QQTcxAj054WP6k4qWxSfKrM0jDuFCZ2HOevuLgKLtfGwLRqDW58hSyH7aq933LwzgaCp8G+r36IA7iUPP9VHbqEVMTR5Icxh7Kl0G8ajou4HCPIpsvyhJIgDH4AJRFHogpt/DgEsIpb+T6DViEpU2mZrw4YZIG4GOeZt5t6JTYIcUoEF8W60emKmpxBT7eR5VQD8mhHYg8MsbbzNQPVlYkcIh30yljEmSqAh3H206BVsn/cqPiPkd55QHgQVuKBb4Fgl7unKbs/AAAAAElFTkSuQmCC>

[image7]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAoAAAAaCAYAAACO5M0mAAAAy0lEQVR4XoVSCw7FIAjTi8j9T+kbILSgySNZ+Fjaum2MiJlV1p4mCs2MQzy2uffV0+CAGqZuYy94SIwYA/oBDPEnihVkc4J9CBVSQ3X5JsngemzVHCJri8iWpdnrggrp9R1EHQsJC25noIOjctWal4KXbGU22Qgnq99aO/NoT/MI41jRPvwGzi5h/siL9vZesXxuKPBW/JF2mC1tn2XYlchOgF2eQOQlsC/WroF/3MF0/mSAJHc3DnGmvFjAZat5SPC1RQYuAk3T//wfLdQmlzieL40AAAAASUVORK5CYII=>

[image8]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAJ4AAAAcCAYAAACQ/QaoAAAEDklEQVR4Xu2YCZLaMBBF4SLD/U+ZlGyEW79/b7LMQCqvyhW7l98LAobcbow7GiJ0wuPx+NOurN1Fy+9Ydotq/JfzNeNujapud4MyO/SDhQfMsp+i0lhnJsdD6SlDSD1DcCoZWKkFXCi9gwerF0T7Z1NbUy26CqhPFZtK+gxk6+wrs9vQZ9nfQW3dtegSKelU0GchWp7sPpeGh4cdJGZrWPaBXBtL0KW0ZTMR839OgjvF5xeb4x5+elXta+Bdc+sCQPh4rFW8bh8z5HuP+75X5GIyh8fyP36anXdz73buPkFRUIUrw4HjysD3dIhy/5OTtTOwEtLm9ncFWNB7nm+Ujf3vYL2Bu136/U343vP4+myGy2DLQT/aGpb9MqydWXaTllBOcol2Ye1WEnUU5XMi1ZGxz1rucqyBLftv8tZViWLRLjIHL+Js/otgSWOdIPgK5LLwK3bZElYPZsgZ5gm0krkPOJg0RoLS8BzmL2JJnSbyA0KpJdx6A7iNRY2tgrw4Y3/Hr/bDZqOnlXBvRrvSg4Wbz1sb6D3IC/Pao1vHQJVnInQJKnMhRBsXkLlaHpFSnyzH02Fj9gyZXNt/NNZ1aP8DdoRdJ4fM9+ayfHZnBCaw20oyF2DVt+wcjKbzbv/tU0e+AEy3gz7sqWG9mBV6PtOPqNSvxL6QTVkCzOYhNc2hTQejFJzm/Ly8r2b1NEyfkLN6Y/TYyiXze1mcxsuR2H5UNGACyta0UA+fBSp/kq5TuVADYXHMViXKj/yNFX3g3+qzRDtlvv1IOAdDwgSkDX0Rs7lbu8meLTLp2Xk32/PrF+/biys1+r33omNNButtJzPZzpY/sUxWG58lni+FVbDbRl99mH5fy8yiVbVl5JjtiHzZ7np2dt9y0T76NY/Hj+nrRBoZen60B+R4M417ESEDns+s3R1tGbg4vIbEDVN2gOdmsznZ3FccJOBs7MJ4ds+eNWNxpt/BHrzYCJWXXBrWVjpA5HfJFOjI2O3++dXT3ylSR8ZthuTwAzM5AUefOXE2k/VsIkqlc148k7128c01+etcCTng653m+MTLJcuDxO5ZDPrnSC5DhSnDRqUfGdvUrFmPCAk+71TqK7ikIvOVHkuNERhfmQNzNyoCjRZvHVp8noJ0SUwJeFalR4zFg9cvGZOB5/B+PxU+A4GNNbM4XD71sWJVVmgAM/O6OD16nxe5TyRHvBG4Y1AAn0ekd+kOM2BBdgi3f/0ZPpPLeubCuMt3wbu5OY4R1Xcyj5DPxKJ48PovZBnzPRx7kBvJb+fNOI05LiAXmYtKQsWo8ZO4Dz3+XrtQOWxkDwjDvoGVQ9xXik1ydQtT+qWkUvCFrO5jtd6T8I9Yg7ms24nEAFf3Hviv53fLr6i+QmPnL7yrABFqzR8uAAAAAElFTkSuQmCC>

[image9]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAsAAAAbCAYAAACqenW9AAAA6klEQVR4Xo1TURaDMAjTi7T3P6UbIYHQ+THetISkgeq8ruvGL+JGQoBCEW+R1RsiXi4Ewdq7wTXJIZShF1pofkyxmMaqShKko+0i7o2tHZEHRVJes4H39y6K2cIK575oEcna+1l7PTvWtXP9Xhv5eqCKWwAaIELojtVZhMYLLC6DbM/aebb0IOq39KdY7UWM+e1/w3HiiA01s+3/QVjw+NbXmfPBS4rSE4Q4knqndag2zOIxTnkORxL6CFw64qegKKLbt7ZrvCfrZiVRkbKmLEaz8XkdcfDunQsEzr+1TFF6JT6MBBwilyHXD1HZGoOt3xzWAAAAAElFTkSuQmCC>

[image10]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAaCAYAAACzdqxAAAABbElEQVR4XpVUC3YEIQgbL+Lc/5TbgnxCwH1tWmeUT4jozvMIlj7/AAuk+C/pgwtNPpe3zi/Maz3yF4uqZM2kOGcdrTA6tMAEtrfsb/AtrOd9388Z2959YBZQ9HK8QyXYQmAW2E2Quys8EyLIVe/PNmWcyKoVEcTRhy/mmFxc4du6GxUCyonWOgWeVMQKkliKeMqJwtie90hvow2aLI+l9qNUHCXlYiKLKBJiV6aEO29IRraNX9QbOsGBhB7Vr7Yhre01I0iHqG13G31aKJcACjrEfvVrStmNufruvCHxrVimyA5okIyFo//DLhJeXQ+KD+g4kfS40p4iiN2TeOTtwD7WYmrRpf9uC2B599hiHaZ1ObgQ73fHk/4BV+zva34rdhbjp1pM3ib2GSpJA2zIhz7HUDZiGzLbMAa3aRYLIycOqAk5dS2gCSZVoh54mHpR/1xWIxsEUyCgth0XIIZmfq8BsKBqnHyD3qjf/x/mcWlt8swQLQAAAABJRU5ErkJggg==>

---
### Archivo Histórico Recuperado

# El Nudo Gordiano: Live Executable Paper

> [!CAUTION]
> ### ⚠️ ALERTA DE SISTEMA: ENTROPÍA ECONÓMICA DETECTADA
> **Este documento no es una simple simulación; es la autopsia en tiempo real del poder adquisitivo bajo fricción fiscal en Chile.** 
> *Actualización automatizada de vectores vía mindicador.cl.*

> [!CAUTION]
> ### ALERTA DE SISTEMA: ENTROPÍA ECONÓMICA DETECTADA
> Este documento no es una simple simulación; es la autopsia en tiempo real del poder adquisitivo bajo fricción fiscal.

El Nudo Gordiano: Anatomía del Derroche Fiscal en Chile

[![Reproducibility: Executable Paper](https://img.shields.io/badge/Reproducibility-Executable_Paper-0052cc)](#-reproducibilidad-computacional)

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
cd nudo-gordiano-economia-cl
python -m venv venv
source venv/bin/activate  # o venv\Scripts\activate en Windows

# 2. Instalar dependencias del motor matemático
pip install numpy pandas scipy

# 3. Ejecutar simulación base (sobrescribe data/simulacion_base.csv)
python src/simulador.py --iterations 10000 --seed 42
```

---

## 🛠️ Infraestructura de Automatización (Live Engine)
Este paper se recalibra dinámicamente utilizando el siguiente stack:
- **Motor de Ingesta**: `src/fetch_data.py` - Captura semanal de UF, UTM e IPC para ajuste de base monetaria simulada.
- **Simulador Dinámico**: `src/simulador.py` - Motor de Monte Carlo que integra `data/live_indicators.json` para proyecciones de estrés financiero.
- **Visualización**: Dashboard brutalista en `index.html` con inyección de datos en tiempo real.
