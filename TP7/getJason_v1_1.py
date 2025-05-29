"""
getJason_v1_1.py - Versión refactorizada 1.1

Copyright © 2024 UADER - FCyT - Ingeniería en Sistemas de Información
Todos los derechos reservados.

Descripción:
Este programa permite cargar un archivo JSON desde línea de comandos
y obtener el valor asociado a una clave. El diseño implementa el
patrón Singleton, se ejecuta desde la línea de comandos con
validación robusta de argumentos y sigue una estrategia de
Branching by Abstraction con una clase base abstracta.

Ejemplo de uso:
    python getJason_v1_1.py sitedata.json token1
"""


import os
import sys
import json
from abc import ABC, abstractmethod


class JsonReaderBase(ABC):
    """Interfaz abstracta para lectores de archivos JSON."""

    @abstractmethod
    def cargar(self):
        """Carga el contenido del archivo JSON."""
        pass

    @abstractmethod
    def obtener_valor(self, clave):
        """Devuelve el valor asociado a una clave específica."""
        pass

class JsonReaderSingleton(JsonReaderBase):
    """Implementación Singleton de lector de archivos JSON."""

    _instancia = None

    def __new__(cls, *args, **kwargs):
        """Crea una única instancia de la clase."""
        if cls._instancia is None:
            cls._instancia = super(JsonReaderSingleton, cls).__new__(cls)
        return cls._instancia

    def __init__(self, ruta_archivo=None):
        """Inicializa la instancia con la ruta del archivo JSON."""
        if not hasattr(self, 'inicializado'):
            self.ruta_archivo = ruta_archivo
            self.datos = {}
            self.inicializado = True

    def cargar(self):
        """Carga el contenido del archivo JSON, con manejo de errores controlado."""
        try:
            with open(self.ruta_archivo, 'r', encoding='utf-8') as archivo:
                self.datos = json.load(archivo)
        except FileNotFoundError:
            print(f"Error controlado: El archivo '{self.ruta_archivo}' no fue encontrado.")
            sys.exit(4)
        except json.JSONDecodeError:
            print(f"Error controlado: El archivo '{self.ruta_archivo}' no tiene formato JSON válido.")
            sys.exit(6)
        except Exception as e:
            print(f"Error inesperado al leer el archivo: {e}")
            sys.exit(7)

    def obtener_valor(self, clave):
        """Obtiene el valor de una clave en el JSON, o un mensaje si no existe."""
        return self.datos.get(clave, f"La clave '{clave}' no se encontró en el archivo.")


def main():
    """Función principal que procesa los argumentos de línea de comandos."""

    # Opción de mostrar versión
    if '-v' in sys.argv or '--version' in sys.argv:
        print("Versión 1.1")
        sys.exit(0)

    # Validar número de argumentos
    if len(sys.argv) < 2:
        print("Uso: python getJason_v1_1.py <archivo_json> [clave]")
        sys.exit(2)

    archivo = sys.argv[1]

    # Validar extensión del archivo
    if not archivo.endswith(".json"):
        print("Error: El archivo debe tener extensión .json")
        sys.exit(3)

    # Validar existencia del archivo
    if not os.path.exists(archivo):
        print(f"Error: El archivo '{archivo}' no existe")
        sys.exit(4)

    # Establecer clave por defecto si no se proporciona
    clave = sys.argv[2] if len(sys.argv) > 2 else "token1"

    try:
        lector: JsonReaderBase = JsonReaderSingleton(archivo)
        lector.cargar()
        resultado = lector.obtener_valor(clave)
        print(resultado)
    except Exception as e:
        print("Error controlado en ejecución:", e)
        sys.exit(5)



if __name__ == "__main__":
    main()
