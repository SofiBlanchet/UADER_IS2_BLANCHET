import json
import sys
import os

class JsonReader:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo
        self.datos = {}

    def cargar(self):
        if not os.path.exists(self.ruta_archivo):
            raise FileNotFoundError(f"No se encuentra el archivo: {self.ruta_archivo}")
        with open(self.ruta_archivo, 'r') as archivo:
            contenido = archivo.read()
            self.datos = json.loads(contenido)

    def obtener_valor(self, clave):
        return self.datos.get(clave, f"Clave '{clave}' no encontrada en el archivo.")

def main():
    if len(sys.argv) < 2:
        print("Uso: python getJason.py <archivo_json> [clave]")
        sys.exit(1)

    archivo = sys.argv[1]
    clave = sys.argv[2] if len(sys.argv) >= 3 else 'token1'

    lector = JsonReader(archivo)
    try:
        lector.cargar()
        resultado = lector.obtener_valor(clave)
        print(resultado)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
