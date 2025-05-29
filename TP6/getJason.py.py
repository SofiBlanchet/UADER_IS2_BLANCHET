import json
import sys

# Verifica si se proporcionaron los argumentos necesarios
if len(sys.argv) < 2:
    print("Uso: python getJason.py <archivo_json> [clave]")
    sys.exit(1)

# Primer argumento: nombre del archivo JSON
jsonfile = sys.argv[1]

# Segundo argumento (opcional): clave a buscar en el JSON
# Si no se especifica, se usa 'token1' por defecto
jsonkey = sys.argv[2] if len(sys.argv) >= 3 else 'token1'

# Abre y lee el contenido del archivo JSON
with open(jsonfile, 'r') as myfile:
    data = myfile.read()

# Convierte el texto JSON a un objeto de Python (diccionario)
obj = json.loads(data)

# Busca la clave solicitada dentro del objeto JSON
if jsonkey in obj:
    print(str(obj[jsonkey]))
else:
    print(f"Clave '{jsonkey}' no encontrada en el archivo.")
