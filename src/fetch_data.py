import requests
import json
import os
from datetime import datetime

def fetch_economic_data():
    print('[*] Consultando indicadores económicos...')
    try:
        # API gratuita para indicadores chilenos
        response = requests.get('https://mindicador.cl/api')
        response.raise_for_status()
        res = response.json()
        
        data = {
            'metadata': {
                'source': 'mindicador.cl',
                'last_update': datetime.now().isoformat()
            },
            'indicators': {
                'uf': res['uf']['valor'],
                'utm': res['utm']['valor'],
                'dolar': res['dolar']['valor'],
                'ipc': res['ipc']['valor']
            }
        }
        
        # Guardar para uso del simulador
        output_path = 'data/live_indicators.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        
        print(f'[+] Datos guardados exitosamente en {output_path}')
        print(f"    UF: ${data['indicators']['uf']} | Dolar: ${data['indicators']['dolar']}")
        
    except Exception as e:
        print(f'[!] Error al capturar datos: {e}')

if __name__ == '__main__':
    fetch_economic_data()