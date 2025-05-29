# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: getJason.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-05-06 19:05:36 UTC (1746558336)

import json
import sys

if len(sys.argv) < 2:
    print("Uso: python getJason.py <archivo_json> [clave]")
    sys.exit(1)

jsonfile = sys.argv[1]
jsonkey = sys.argv[2] if len(sys.argv) >= 3 else 'token1'

with open(jsonfile, 'r') as myfile:
    data = myfile.read()

obj = json.loads(data)

if jsonkey in obj:
    print(str(obj[jsonkey]))
else:
    print(f"Clave '{jsonkey}' no encontrada en el archivo.")
