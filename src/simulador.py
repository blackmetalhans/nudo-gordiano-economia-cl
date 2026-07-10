
import json
import os

def load_live_data():
    path = 'data/live_indicators.json'
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
            print(f'[SYSTEM] Datos en vivo cargados: UF=${data["indicators"]["uf"]}')
            return data['indicators']
    return None

live_params = load_live_data()
# Ejemplo de integración: 
# UF_ACTUAL = live_params['uf'] if live_params else 37000

#!/usr/bin/env python3
"""
Simulador estocástico del Nudo Gordiano – Economía Chile
=========================================================
Regenera data/simulacion_base.csv modelando los cuatro pilares de fricción fiscal:

  Pilar 1 – Fraude del Hormigón   : sobreprecio en obras públicas municipales
  Pilar 2 – Exacción Energética   : traspaso de Brent e impuesto específico al surtidor
  Pilar 3 – Hipertrofia Burocrática: pérdida de eficiencia por capas administrativas
  Pilar 4 – Commoditización        : volatilidad y nivel del precio del crudo (Brent)

Uso básico:
    python src/simulador.py

Escenario con mayor impuesto y más capas burocráticas:
    python src/simulador.py --impuesto-especifico 150 --capas-burocraticas 8

Ver todas las opciones:
    python src/simulador.py --help
"""
import argparse
import csv
import os
import sys

try:
    import numpy as np
except ImportError:
    print("ERROR: numpy no está instalado. Ejecuta: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Parámetros estructurales del modelo (calibrados sobre la serie histórica)
# ---------------------------------------------------------------------------
INGRESO_POTENCIAL_BASE = 1_182_000.0   # CLP bruto mensual antes de fricciones
ALPHA_BRENT = 8.4486                   # sensibilidad precio surtidor al Brent (CLP/litro por USD/barril)
BASE_COMBUSTIBLE = 550.93              # costo base CLP/litro sin impuesto específico
COEF_ENERGIA = 0.12                    # fracción del ingreso bruto afectada por costo energético
COEF_CONSTRUCCION = 0.01               # fracción del ingreso bruto afectada por costo de obra pública
VOL_BRENT_DEFAULT = 12.0               # desviación estándar del Brent (USD)
VOL_SURTIDOR_RUIDO = 15.0              # ruido estocástico adicional en precio surtidor (CLP/litro)
VOL_M2_DEFAULT = 3_000.0               # desviación estándar del costo de obra (CLP/m²)

DEFAULT_OUTPUT = os.path.join(
    os.path.dirname(__file__), "..", "data", "simulacion_base.csv"
)


def calcular_eficiencia(capas: int) -> float:
    """
    Pilar 3 – Hipertrofia Burocrática.
    Cada capa administrativa adicional degrada la eficiencia del aparato estatal.
    Con 5 capas (escenario base) la eficiencia es ≈ 0.55, consistente con la serie histórica.
    """
    return max(0.05, 1.0 - capas * 0.09)


def simular(
    n: int,
    seed: int,
    brent_base: float,
    volatilidad_brent: float,
    impuesto_especifico: float,
    capas_burocraticas: int,
    sobreprecio_construccion: float,
    costo_m2_base: float,
    volatilidad_m2: float,
) -> list:
    """Corre la simulación y devuelve una lista de dicts con los resultados."""
    rng = np.random.default_rng(seed)

    # ------------------------------------------------------------------
    # Pilar 3: eficiencia estructural del aparato estatal
    # ------------------------------------------------------------------
    eficiencia = calcular_eficiencia(capas_burocraticas)
    ingreso_bruto = INGRESO_POTENCIAL_BASE * eficiencia

    # ------------------------------------------------------------------
    # Pilar 4: trayectoria estocástica del Brent
    # ------------------------------------------------------------------
    precio_brent = np.maximum(20.0, rng.normal(brent_base, volatilidad_brent, n))

    # ------------------------------------------------------------------
    # Pilar 2: precio surtidor = traspaso de Brent + impuesto específico + ruido
    # ------------------------------------------------------------------
    precio_surtidor = (
        ALPHA_BRENT * precio_brent
        + BASE_COMBUSTIBLE
        + impuesto_especifico
        + rng.normal(0.0, VOL_SURTIDOR_RUIDO, n)
    )

    # ------------------------------------------------------------------
    # Pilar 1: costo de obra municipal con sobreprecio fraudulento
    # ------------------------------------------------------------------
    media_m2 = costo_m2_base * (1.0 + sobreprecio_construccion / 100.0)
    costo_m2 = np.maximum(15_000.0, rng.normal(media_m2, volatilidad_m2, n))

    # ------------------------------------------------------------------
    # Ingreso neto real del ciudadano
    # ------------------------------------------------------------------
    ingreso_neto = ingreso_bruto - COEF_ENERGIA * precio_surtidor - COEF_CONSTRUCCION * costo_m2

    rows = []
    for i in range(n):
        rows.append(
            {
                "Precio_Brent": precio_brent[i],
                "Precio_Surtidor_Litro": precio_surtidor[i],
                "Costo_M2_Obra_Muni": costo_m2[i],
                "Eficiencia_Aparato_Estatal": eficiencia,
                "Ingreso_Neto_Real_Ciudadano": ingreso_neto[i],
            }
        )
    return rows


def escribir_csv(rows: list, path: str) -> None:
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    campos = [
        "Precio_Brent",
        "Precio_Surtidor_Litro",
        "Costo_M2_Obra_Muni",
        "Eficiencia_Aparato_Estatal",
        "Ingreso_Neto_Real_Ciudadano",
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(rows)


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description=(
            "Simulador del Nudo Gordiano – regenera data/simulacion_base.csv "
            "con parámetros ajustables para cada pilar de fricción fiscal."
        ),
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    sim = parser.add_argument_group("Parámetros de simulación")
    sim.add_argument(
        "--n",
        type=int,
        default=1000,
        metavar="FILAS",
        help="Número de observaciones a generar.",
    )
    sim.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Semilla aleatoria para reproducibilidad.",
    )
    sim.add_argument(
        "--output",
        type=str,
        default=DEFAULT_OUTPUT,
        metavar="RUTA",
        help="Ruta del archivo CSV de salida.",
    )

    p1 = parser.add_argument_group(
        "Pilar 1 – Fraude del Hormigón (sobreprecio en obras municipales)"
    )
    p1.add_argument(
        "--sobreprecio-construccion",
        type=float,
        default=0.0,
        metavar="PCT",
        help=(
            "Porcentaje de sobreprecio en obras municipales respecto al costo base. "
            "Ej: 20 implica un 20% de sobrecosto fraudulento."
        ),
    )
    p1.add_argument(
        "--costo-m2-base",
        type=float,
        default=30_000.0,
        metavar="CLP",
        help="Costo base por m² de obra municipal (CLP) antes de sobreprecio.",
    )
    p1.add_argument(
        "--volatilidad-m2",
        type=float,
        default=VOL_M2_DEFAULT,
        metavar="CLP",
        help="Desviación estándar del costo por m² (CLP).",
    )

    p2 = parser.add_argument_group(
        "Pilar 2 – Exacción Energética (impuesto específico a combustibles)"
    )
    p2.add_argument(
        "--impuesto-especifico",
        type=float,
        default=0.0,
        metavar="CLP/L",
        help=(
            "Impuesto específico adicional al combustible (CLP/litro). "
            "Se suma al costo base de distribución."
        ),
    )

    p3 = parser.add_argument_group(
        "Pilar 3 – Hipertrofia Burocrática (capas administrativas)"
    )
    p3.add_argument(
        "--capas-burocraticas",
        type=int,
        default=5,
        metavar="N",
        help=(
            "Número de capas administrativas del aparato estatal. "
            "Cada capa adicional reduce la Eficiencia_Aparato_Estatal en 0.09 puntos."
        ),
    )

    p4 = parser.add_argument_group(
        "Pilar 4 – Commoditización (exposición al precio del crudo)"
    )
    p4.add_argument(
        "--brent-base",
        type=float,
        default=75.0,
        metavar="USD",
        help="Precio medio del Brent (USD/barril) alrededor del cual oscila la simulación.",
    )
    p4.add_argument(
        "--volatilidad-brent",
        type=float,
        default=VOL_BRENT_DEFAULT,
        metavar="USD",
        help="Volatilidad del Brent (desviación estándar, USD/barril).",
    )

    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)

    print("Ejecutando simulación con parámetros:")
    print(f"  Filas              : {args.n}")
    print(f"  Semilla            : {args.seed}")
    print(f"  Brent base         : {args.brent_base} USD/barril")
    print(f"  Volatilidad Brent  : {args.volatilidad_brent} USD")
    print(f"  Impuesto específico: {args.impuesto_especifico} CLP/litro")
    print(f"  Capas burocráticas : {args.capas_burocraticas}  → "
          f"Eficiencia = {calcular_eficiencia(args.capas_burocraticas):.4f}")
    print(f"  Sobreprecio obra   : {args.sobreprecio_construccion}%")
    print(f"  Costo m² base      : {args.costo_m2_base:,.0f} CLP")
    print(f"  Salida             : {args.output}")

    rows = simular(
        n=args.n,
        seed=args.seed,
        brent_base=args.brent_base,
        volatilidad_brent=args.volatilidad_brent,
        impuesto_especifico=args.impuesto_especifico,
        capas_burocraticas=args.capas_burocraticas,
        sobreprecio_construccion=args.sobreprecio_construccion,
        costo_m2_base=args.costo_m2_base,
        volatilidad_m2=args.volatilidad_m2,
    )

    escribir_csv(rows, args.output)

    ingresos = [r["Ingreso_Neto_Real_Ciudadano"] for r in rows]
    media = sum(ingresos) / len(ingresos)
    print(f"\nIngreso_Neto_Real_Ciudadano – media: {media:,.2f} CLP")
    print(f"Simulación completa. CSV guardado en: {args.output}")


if __name__ == "__main__":
    main()
import numpy as np

def apply_black_swan_shocks(base_value, probability=0.07):
    """Inyecta eventos de baja probabilidad y alto impacto, señalando el origen de la crisis."""
    if np.random.rand() < probability:
        # Diccionario de causas raíz para no perder el sentido científico
        shocks = {
            'HIPERINFLACIÓN_ESTRUCTURAL': {'sev': 2.5, 'causa': 'Emisión descontrolada y pérdida de confianza fiscal'},
            'COLAPSO_COBRE_BRENT': {'sev': 1.8, 'causa': 'Shock externo en matriz de ingresos/costos energéticos'},
            'CRISIS_BUROCRÁTICA_TOTAL': {'sev': 2.1, 'causa': 'Parálisis por ineficiencia en administración pública'}
        }
        
        type_key = np.random.choice(list(shocks.keys()))
        event = shocks[type_key]
        severity = np.random.uniform(1.2, event['sev'])
        
        print(f'[⚠️ CISNE NEGRO DETECTADO]')
        print(f'   ORIGEN: {type_key}')
        print(f'   DIAGNÓSTICO: {event["causa"]}')
        print(f'   MAGNITUD: x{severity:.2f} de erosión adicional.')
        
        return base_value * severity
    return base_value
